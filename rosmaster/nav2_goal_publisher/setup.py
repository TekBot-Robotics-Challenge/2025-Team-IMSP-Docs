from setuptools import setup

package_name = 'nav2_goal_publisher'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/send_goal.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='you',
    maintainer_email='you@example.com',
    description='Send a Nav2 NavigateToPose action goal',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'send_goal = nav2_goal_publisher.send_goal_node:main',
        ],
    },
)
