#!/usr/bin/env python
# encoding: utf-8

#public lib
import os
import time
import getpass
import threading
from time import sleep

#ros lib
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from actionlib_msgs.msg import GoalID
from std_msgs.msg import Int32, Bool
from std_srvs.srv import Trigger

class JoyTeleop(Node):
	"""
	JoyTeleop
	ROS 2 node that converts joystick (sensor_msgs/Joy) input into robot control commands
	# and control signals (cmd_vel, Buzzer, RGBLight, JoyState). It supports two input
	mappings depending on the running user (root -> "jetson" mapping, otherwise "pc" mapping).
	Public behavior and side effects
	- Subscribes: 'joy' (sensor_msgs.msg.Joy)
	- Publishes:
		- 'cmd_vel' (geometry_msgs.msg.Twist) — movement commands (published multiple times to improve delivery)
		- 'move_base/cancel' (actionlib_msgs.msg.GoalID) — reserved publisher, not actively used in current code
		# # - 'Buzzer' (std_msgs.msg.Bool) — toggle buzzer on/off
		- 'JoyState' (std_msgs.msg.Bool) — publishes whether joystick control is active
		- 'RGBLight' (std_msgs.msg.Int32) — index for RGB light patterns
	Parameters (declared with defaults)
	- xspeed_limit (double, default 1.0): maximum linear.x speed
	- yspeed_limit (double, default 1.0): maximum linear.y speed
	- angular_speed_limit (double, default 5.0): maximum angular.z speed
	Key attributes
	- Joy_active (bool): whether joystick-based velocity commands are allowed/published
	# # - Buzzer_active (bool): current buzzer state
	- RGBLight_index (int): current index for RGB light patterns (cycles 0..5)
	- linear_Gear (float): scaling factor for linear speeds (cycles through 1, 1/3, 2/3)
	- angular_Gear (float): scaling factor for angular speed (cycles through 1, 1/4, 1/2, 3/4)
	- cancel_time (float): timestamp used to debounce cancel/toggle actions
	- user_name (str): getpass.getuser(), used to select mapping (root => jetson mapping)
	Input mapping and behavior details
	- Movement axes (after deadzone filtering via filter_data):
		- x linear speed is read from axes[1]
		- y linear speed is read from axes[0]
		- angular speed is read from axes[2]
		- Each speed is scaled by the corresponding limit parameter and current gear.
		- Speeds are clamped to ±their respective limits.
		- If Joy_active is True, a Twist with these speeds is published to 'cmd_vel' (typically published 3 times in places in the code).
	- Toggle joystick control / "cancel" behavior (cancel_nav)
		- Jetson mapping: cancel triggered by axes[9] == 1
		- PC mapping: cancel triggered by axes[5] == -1
		- cancel_nav toggles Joy_active, publishes JoyState (std_msgs/Bool) and a zero Twist to 'cmd_vel'
			and enforces a 1 second debounce between toggles.
	- RGBLight control
		- Jetson mapping: button index 7
			- Publishes an Int32 with the current RGBLight_index three times, then increments index (wraps to 0 at 6)
		- PC mapping: button index 5
			- Publishes current index once, then increments (wraps at 6)
	# - Buzzer control
		# - Jetson mapping: button index 11 — toggles Buzzer_active and publishes Bool three times
		# - PC mapping: button index 7 — toggles Buzzer_active and publishes Bool once
	- Gear control (scales applied to speeds)
		- Linear gear:
			- Jetson: button 13; PC: button 9
			- Cycle order: 1.0 -> 1/3 -> 2/3 -> 1.0
		- Angular gear:
			- Jetson: button 14; PC: button 10
			- Cycle order: 1.0 -> 1/4 -> 1/2 -> 3/4 -> 1.0
	Helper methods
	- filter_data(value): applies a deadzone; returns 0 if abs(value) < 0.2 else returns value
	- cancel_nav(): toggles Joy_active with a 1s debounce, publishes JoyState and zero cmd_vel messages
	Assumptions and notes
	- The class assumes specific joystick axis/button index mappings; these must match the connected joystick.
	- Many messages are published multiple times (3x) in some branches to increase likelihood of delivery.
	- The move_base/cancel publisher exists but the GoalID publish line is commented out in cancel_nav.
	"""
	def __init__(self,name):
		super().__init__(name)
		self.Joy_active = False
		# self.Buzzer_active = False
		# self.RGBLight_index = 0
		self.cancel_time = time.time()
		self.user_name = getpass.getuser()
		self.linear_Gear = 1
		self.angular_Gear = 1
		
		#create pub
		self.pub_goal = self.create_publisher(GoalID,"move_base/cancel",10)
		self.pub_cmdVel = self.create_publisher(Twist,'cmd_vel',  10)
		# self.pub_Buzzer = self.create_publisher(Bool,"Buzzer",  1)
		self.pub_JoyState = self.create_publisher(Bool,"JoyState",  10)
		# self.pub_RGBLight = self.create_publisher(Int32,"RGBLight" , 10)
		
		#create sub
		self.sub_Joy = self.create_subscription(Joy,'joy', self.buttonCallback,10)

		#declare parameter and get the value
		self.declare_parameter('xspeed_limit',1.0)
		self.declare_parameter('yspeed_limit',1.0)
		self.declare_parameter('angular_speed_limit',5.0)
		self.xspeed_limit = self.get_parameter('xspeed_limit').get_parameter_value().double_value
		self.yspeed_limit = self.get_parameter('yspeed_limit').get_parameter_value().double_value
		self.angular_speed_limit = self.get_parameter('angular_speed_limit').get_parameter_value().double_value

		
	def buttonCallback(self,joy_data):
		if not isinstance(joy_data, Joy): return
		
		# Print currently pressed buttons and active axes
		active_buttons = [i for i, btn in enumerate(joy_data.buttons) if btn == 1]
		active_axes = [i for i, axis in enumerate(joy_data.axes) if abs(axis) > 0.2]
		# if active_buttons or active_axes:
		# 	self.get_logger().info(f"Buttons: {active_buttons}, Axes: {active_axes}")

		if self.user_name == "root": self.user_jetson(joy_data)
		else: self.user_pc(joy_data)
		
	def user_jetson(self, joy_data):
		#cancel nav
		if joy_data.axes[9] == 1: self.cancel_nav()
        #linear Gear control
		if joy_data.buttons[13] == 1:
			if self.linear_Gear == 1.0: self.linear_Gear = 1.0 / 3
			elif self.linear_Gear == 1.0 / 3: self.linear_Gear = 2.0 / 3
			elif self.linear_Gear == 2.0 / 3: self.linear_Gear = 1
        # angular Gear control
		if joy_data.buttons[14] == 1:
			if self.angular_Gear == 1.0: self.angular_Gear = 1.0 / 4
			elif self.angular_Gear == 1.0 / 4: self.angular_Gear = 1.0 / 2
			elif self.angular_Gear == 1.0 / 2: self.angular_Gear = 3.0 / 4
			elif self.angular_Gear == 3.0 / 4: self.angular_Gear = 1.0

		

		xlinear_speed = self.filter_data(joy_data.axes[1]) * self.xspeed_limit * self.linear_Gear
        # ylinear_speed = self.filter_data(joy_data.axes[2]) * self.yspeed_limit * self.linear_Gear
		ylinear_speed = self.filter_data(joy_data.axes[0]) * self.yspeed_limit * self.linear_Gear
		angular_speed = self.filter_data(joy_data.axes[2]) * self.angular_speed_limit * self.angular_Gear
		if xlinear_speed > self.xspeed_limit: xlinear_speed = self.xspeed_limit
		elif xlinear_speed < -self.xspeed_limit: xlinear_speed = -self.xspeed_limit

		if ylinear_speed > self.yspeed_limit: ylinear_speed = self.yspeed_limit
		elif ylinear_speed < -self.yspeed_limit: ylinear_speed = -self.yspeed_limit

		if angular_speed > self.angular_speed_limit: angular_speed = self.angular_speed_limit
		elif angular_speed < -self.angular_speed_limit: angular_speed = -self.angular_speed_limit

		twist = Twist()
		twist.linear.x = xlinear_speed
		twist.linear.y = ylinear_speed
		twist.angular.z = angular_speed
		if self.Joy_active == True:
			print("joy control now")
			for i in range(3): self.pub_cmdVel.publish(twist)
        
	def user_pc(self, joy_data):

        # 取消 Cancel
		if joy_data.axes[5] == -1: self.cancel_nav()
		
		# if joy_data.buttons[5] == 1:
		# 	if self.RGBLight_index < 6:
		# 		self.pub_RGBLight.publish(self.RGBLight_index)
        #         # print ("pub RGBLight success")
		# 	else: self.RGBLight_index = 0
		# 	self.RGBLight_index += 1
		if joy_data.buttons[5] == 1:
			print("Pressing R1 button ")

		if joy_data.buttons[7] == 1:
			print("Pressing R2 button ")

		# if joy_data.buttons[7] == 1:
		# 	self.Buzzer_active=not self.Buzzer_active
        #     # print "self.Buzzer_active: ", self.Buzzer_active
		# 	self.pub_Buzzer.publish(self.Buzzer_active)

        # 档位控制 Gear control
		if joy_data.buttons[9] == 1:
			if self.linear_Gear == 1.0: self.linear_Gear = 1.0 / 3
			elif self.linear_Gear == 1.0 / 3: self.linear_Gear = 2.0 / 3
			elif self.linear_Gear == 2.0 / 3: self.linear_Gear = 1

		if joy_data.buttons[10] == 1:
			if self.angular_Gear == 1.0: self.angular_Gear = 1.0 / 4
			elif self.angular_Gear == 1.0 / 4: self.angular_Gear = 1.0 / 2
			elif self.angular_Gear == 1.0 / 2: self.angular_Gear = 3.0 / 4
			elif self.angular_Gear == 3.0 / 4: self.angular_Gear = 1.0

		xlinear_speed = self.filter_data(joy_data.axes[1]) * self.xspeed_limit * self.linear_Gear
		ylinear_speed = self.filter_data(joy_data.axes[0]) * self.yspeed_limit * self.linear_Gear
		angular_speed = self.filter_data(joy_data.axes[2]) * self.angular_speed_limit * self.angular_Gear
		
		if xlinear_speed > self.xspeed_limit: xlinear_speed = self.xspeed_limit
		elif xlinear_speed < -self.xspeed_limit: xlinear_speed = -self.xspeed_limit
		
		if ylinear_speed > self.yspeed_limit: ylinear_speed = self.yspeed_limit
		elif ylinear_speed < -self.yspeed_limit: ylinear_speed = -self.yspeed_limit
		
		if angular_speed > self.angular_speed_limit: angular_speed = self.angular_speed_limit
		elif angular_speed < -self.angular_speed_limit: angular_speed = -self.angular_speed_limit
		
		twist = Twist()
		twist.linear.x = xlinear_speed
		twist.linear.y = ylinear_speed
		twist.angular.z = angular_speed
		
		for i in range(3): self.pub_cmdVel.publish(twist)
        
	def filter_data(self, value):
		if abs(value) < 0.2: value = 0
		return value
		
	def cancel_nav(self):
		now_time = time.time()
		if now_time - self.cancel_time > 1:
			Joy_ctrl = Bool()
			self.Joy_active = not self.Joy_active
			Joy_ctrl.data = self.Joy_active
			for i in range(3):
				self.pub_JoyState.publish(Joy_ctrl)
				#self.pub_goal.publish(GoalID())
				self.pub_cmdVel.publish(Twist())
			self.cancel_time = now_time
			
def main():
	rclpy.init()
	joy_ctrl = JoyTeleop('joy_ctrl')
	rclpy.spin(joy_ctrl)


if __name__ == "__main__":
    main()	
