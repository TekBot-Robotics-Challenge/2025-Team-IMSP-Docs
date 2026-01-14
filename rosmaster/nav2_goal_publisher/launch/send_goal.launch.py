from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    goal_x = LaunchConfiguration('goal_x', default='1.0')
    goal_y = LaunchConfiguration('goal_y', default='0.0')
    goal_yaw = LaunchConfiguration('goal_yaw', default='0.0')
    frame_id = LaunchConfiguration('frame_id', default='map')
    goals_yaml = LaunchConfiguration('goals_yaml', default='')
    halt_on_failure = LaunchConfiguration('halt_on_failure', default='false')

    return LaunchDescription([
        DeclareLaunchArgument('goal_x', default_value=goal_x, description='Goal X'),
        DeclareLaunchArgument('goal_y', default_value=goal_y, description='Goal Y'),
        DeclareLaunchArgument('goal_yaw', default_value=goal_yaw, description='Goal yaw (rad)'),
        DeclareLaunchArgument('frame_id', default_value=frame_id, description='Goal frame'),
        DeclareLaunchArgument('goals_yaml', default_value=goals_yaml, description='Path to YAML file with goals list'),
        DeclareLaunchArgument('halt_on_failure', default_value=halt_on_failure, description='Stop sequence on failure (true/false)'),

        Node(
            package='nav2_goal_publisher',
            executable='send_goal',
            name='nav2_goal_publisher',
            output='screen',
            parameters=[{
                'goal_x': goal_x,
                'goal_y': goal_y,
                'goal_yaw': goal_yaw,
                'frame_id': frame_id,
                'auto_send': True,
                'goals_yaml': goals_yaml,
                'halt_on_failure': halt_on_failure,
            }]
        )
    ])
