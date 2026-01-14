# nav2_goal_publisher

Tiny ROS 2 (Humble) Python package that sends a Nav2 `NavigateToPose` goal.

For the full architecture and design rationale, see [DESIGN.md](./DESIGN.md).

Version française : [DESIGN.fr.md](./DESIGN.fr.md)

## Build

This repo is symlinked into `~/trc_ws/src` by `configure.sh`. You can use that script or build manually:

```bash
source /opt/ros/humble/setup.bash
cd ~/trc_ws
colcon build --packages-select nav2_goal_publisher
source install/setup.bash
```

## Run

Ensure Nav2 bringup is running and localized in the `map` frame, then:

```bash
ros2 launch nav2_goal_publisher send_goal.launch.py goal_x:=2.0 goal_y:=1.0 goal_yaw:=1.57 frame_id:=map
```

Or run the node directly (parameters via CLI):

```bash
ros2 run nav2_goal_publisher send_goal --ros-args -p goal_x:=2.0 -p goal_y:=1.0 -p goal_yaw:=1.57 -p frame_id:=map
```

### Multiple goals from YAML

You can provide a YAML file to send a sequence of goals. Schema:

```yaml
goals:
	- { x: 2.0, y: 1.0, yaw: 1.57, frame_id: map }
	- { x: 0.0, y: 0.0, yaw: 0.0 }           # frame_id defaults to the node parameter (map)
```

Launch with the YAML path:

```bash
ros2 launch nav2_goal_publisher send_goal.launch.py goals_yaml:=/absolute/path/to/goals.yaml halt_on_failure:=false
```

You can also run via `ros2 run`:

```bash
ros2 run nav2_goal_publisher send_goal --ros-args -p goals_yaml:=/absolute/path/to/goals.yaml -p halt_on_failure:=true
```

Notes:
- When `goals_yaml` is given, the single-goal parameters (`goal_x`, `goal_y`, `goal_yaw`, `frame_id`) are ignored.
- `halt_on_failure` (true/false) stops the sequence if a goal is rejected or fails.
 - Relative paths are resolved by the current working directory of the node; prefer absolute paths in launch files.
