from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='x3_control',
            executable='qr_service_node.py',
            name='qr_service_node',
            output='screen',
            parameters=[{
                'camera_index': 1,
                'show_window': False,
                'quartiers_file': 'quartiers.yml'
            }]
        )
    ])
