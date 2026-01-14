import math
import os
from typing import List, Dict, Any

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped


class Nav2GoalPublisher(Node):
    def __init__(self):
        super().__init__('nav2_goal_publisher')

        self.declare_parameter('goal_x', 0.0)
        self.declare_parameter('goal_y', 0.0)
        self.declare_parameter('goal_yaw', 0.0)  # radians
        self.declare_parameter('frame_id', 'map')
        self.declare_parameter('auto_send', True)
        self.declare_parameter('goals_yaml', '')  # path to YAML file listing goals
        self.declare_parameter('halt_on_failure', False)

        self._client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

        # Internal state for YAML-driven sequences
        self._goals: List[Dict[str, Any]] = []
        self._goal_idx: int = 0
        self._sent = False

        # Load YAML goals if provided
        yaml_path = self.get_parameter('goals_yaml').get_parameter_value().string_value
        if yaml_path:
            self._load_goals_yaml(yaml_path)
        if self.get_parameter('auto_send').get_parameter_value().bool_value:
            self.timer = self.create_timer(0.2, self._try_send_once)

    def _try_send_once(self):
        if self._sent:
            return
        if not self._client.wait_for_server(timeout_sec=0.1):
            self.get_logger().info('Waiting for navigate_to_pose action server...')
            return
        self._sent = True
        try:
            self.timer.cancel()
        except Exception:
            pass
        # Decide between YAML-driven sequence or single param goal
        if self._goals:
            self._send_next_goal()
        else:
            self.send_goal_from_params()

    def send_goal_from_params(self):
        x = self.get_parameter('goal_x').get_parameter_value().double_value
        y = self.get_parameter('goal_y').get_parameter_value().double_value
        yaw = self.get_parameter('goal_yaw').get_parameter_value().double_value
        frame_id = self.get_parameter('frame_id').get_parameter_value().string_value

        goal_msg = self._build_goal(x=x, y=y, yaw=yaw, frame_id=frame_id)
        self.get_logger().info(f'Sending goal to ({x:.2f}, {y:.2f}) yaw {yaw:.2f} rad in {frame_id}')
        self._send_goal(goal_msg)

    def _build_goal(self, x: float, y: float, yaw: float, frame_id: str) -> NavigateToPose.Goal:
        qz = math.sin(yaw / 2.0)
        qw = math.cos(yaw / 2.0)

        pose = PoseStamped()
        pose.header.frame_id = frame_id
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.orientation.z = qz
        pose.pose.orientation.w = qw

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose
        return goal_msg

    def _send_goal(self, goal_msg: NavigateToPose.Goal):
        send_future = self._client.send_goal_async(
            goal_msg,
            feedback_callback=self._feedback_cb
        )
        send_future.add_done_callback(self._goal_response_cb)

    def _goal_response_cb(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().warn('Goal rejected')
            if self._goals:
                if self.get_parameter('halt_on_failure').get_parameter_value().bool_value:
                    self.get_logger().warn('Halting on failure (rejected).')
                    rclpy.shutdown()
                    return
                self._advance_and_maybe_send_next()
            return
        self.get_logger().info('Goal accepted')
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self._result_cb)

    def _feedback_cb(self, feedback_msg):
        fb = feedback_msg.feedback
        # Print minimal feedback to avoid spam; change to debug for more verbosity
        self.get_logger().debug(f'Feedback: distance_remaining={getattr(fb, "distance_remaining", "?")}')

    def _result_cb(self, future):
        try:
            result = future.result()
            status = getattr(result, 'status', None)
            self.get_logger().info(f'Navigation finished. status={status} result={getattr(result, "result", None)}')
        except Exception as e:
            self.get_logger().error(f'Failed to get result: {e}')
            if self._goals and self.get_parameter('halt_on_failure').get_parameter_value().bool_value:
                self.get_logger().warn('Halting on failure (exception).')
                rclpy.shutdown()
                return

        if self._goals:
            self._advance_and_maybe_send_next()
        else:
            rclpy.shutdown()

    # --- YAML goals handling ---
    def _load_goals_yaml(self, path: str) -> None:
        path = os.path.expanduser(path)
        if not os.path.isfile(path):
            self.get_logger().error(f'goals_yaml file not found: {path}')
            return
        try:
            import yaml  # type: ignore
        except Exception as e:
            self.get_logger().error(
                f'Failed to import yaml. Ensure python3-yaml is installed. Error: {e}'
            )
            return
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
        except Exception as e:
            self.get_logger().error(f'Failed to read YAML file {path}: {e}')
            return

        goals = data.get('goals', [])
        if not isinstance(goals, list):
            self.get_logger().error('YAML format error: expected a list under "goals"')
            return

        normalized: List[Dict[str, Any]] = []
        for i, g in enumerate(goals):
            if not isinstance(g, dict):
                self.get_logger().warn(f'Ignoring non-dict goal at index {i}: {g!r}')
                continue
            try:
                x = float(g.get('x'))
                y = float(g.get('y'))
                yaw = float(g.get('yaw', 0.0))  # radians
                frame_id = str(g.get('frame_id', self.get_parameter('frame_id').get_parameter_value().string_value))
            except Exception as e:
                self.get_logger().warn(f'Invalid goal at index {i}: {e}. Entry: {g!r}')
                continue
            normalized.append({'x': x, 'y': y, 'yaw': yaw, 'frame_id': frame_id})

        self._goals = normalized
        self._goal_idx = 0
        self.get_logger().info(f'Loaded {len(self._goals)} goals from YAML.')

    def _send_next_goal(self) -> None:
        if self._goal_idx >= len(self._goals):
            self.get_logger().info('All goals processed. Shutting down.')
            rclpy.shutdown()
            return
        g = self._goals[self._goal_idx]
        goal_msg = self._build_goal(x=g['x'], y=g['y'], yaw=g['yaw'], frame_id=g['frame_id'])
        self.get_logger().info(
            f'Sending goal #{self._goal_idx + 1}/{len(self._goals)} to ({g["x"]:.2f}, {g["y"]:.2f}) yaw {g["yaw"]:.2f} in {g["frame_id"]}'
        )
        self._send_goal(goal_msg)

    def _advance_and_maybe_send_next(self) -> None:
        self._goal_idx += 1
        self._send_next_goal()


def main():
    rclpy.init()
    node = Nav2GoalPublisher()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
