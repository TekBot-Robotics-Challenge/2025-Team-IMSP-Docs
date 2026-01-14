# nav2_goal_publisher – Design & Rationale

This document explains how the `nav2_goal_publisher` package is implemented and justifies the key technical choices. The goal of the package is to send a single Nav2 `NavigateToPose` action goal in a clean, composable way suitable for both quick experiments and integration into larger systems.

## Objectives

- Provide a tiny, dependency-light node that sends a Nav2 goal reliably.
- Make the goal specification ergonomic via parameters and launch arguments.
- Keep the implementation idiomatic for ROS 2 Humble with clear extension points.

## Package layout

```
nav2_goal_publisher/
  package.xml                 # ament_python metadata & runtime deps
  setup.py                    # packaging, console_scripts entry point
  setup.cfg                   # install locations for console scripts
  resource/
    nav2_goal_publisher       # required by ament index
  launch/
    send_goal.launch.py       # parameterized launch for the node
  nav2_goal_publisher/
    __init__.py
    send_goal_node.py         # rclpy ActionClient to NavigateToPose
  README.md                   # quick usage
  DESIGN.md                   # this document
```

## Why Python and `ament_python`

- Simplicity and speed: For a single action client with no heavy computation, Python (`rclpy`) avoids boilerplate and C++ toolchain complexity.
- Faster iteration: No compile-link cycles; just rebuild the package metadata. Great for rapid testing.
- Standard ROS 2 pattern: Pure-Python nodes are first-class citizens and integrate seamlessly with `colcon` and the ament index via `ament_python`.

Alternatives considered:
- `rclcpp` + `ament_cmake`: Heavier setup for minimal gain here.
- CLI-only (e.g., `ros2 action send_goal`): Good for one-offs but not as composable/parametric as a node you can include in launch files.

## Dependencies and justification

- `rclpy`: ROS 2 Python client library to create the node and interact with actions.
- `nav2_msgs`: Provides the `NavigateToPose` action definition.
- `geometry_msgs`: For the `PoseStamped` goal payload.
- `launch`, `launch_ros`: To expose clean CLI/launch-time parameterization.
- `python3-yaml`: Runtime YAML parser used to load sequences of goals from a file.

These are declared as `exec_depend` in `package.xml` because they are runtime requirements for a Python-only package.

## Node design

File: `nav2_goal_publisher/send_goal_node.py`

- Node name: `nav2_goal_publisher` (descriptive and consistent with package name).
- Action: `navigate_to_pose` using `ActionClient(NavigateToPose)`.
- Parameters (with defaults):
  - `goal_x` (float, default 0.0)
  - `goal_y` (float, default 0.0)
  - `goal_yaw` (float, radians, default 0.0)
  - `frame_id` (string, default `map`)
  - `auto_send` (bool, default `True`)
  - `goals_yaml` (string, default ""): absolute or relative path to a YAML file with a list of goals
  - `halt_on_failure` (bool, default `False`): when true, stop the YAML sequence on rejection/failure

### Waiting for the action server: timer-based single-shot

- Strategy: Create a short periodic timer (200ms) that checks `wait_for_server(timeout_sec=0.1)` and sends the goal once the server is available.
- Why a timer and not a blocking wait? The timer keeps the node responsive and avoids blocking the executor before the action server is up. This is an idiomatic rclpy pattern for one-shot start-up behavior.

### Goal pose construction

- Orientation is built from yaw only to keep the interface simple:
  - $q_z = \sin(\text{yaw}/2)$, $q_w = \cos(\text{yaw}/2)$.
- The header uses `frame_id` (default `map`) and the node stamp time to be current.

### Feedback and result handling

- Feedback: Logs a succinct line (e.g., `distance_remaining`) to avoid console spam while still being informative.
- Result: On completion (or rejection), the node logs the outcome.
  - Single-goal mode: calls `rclpy.shutdown()` and exits.
  - YAML sequence: advances to the next goal; if `halt_on_failure` is true and a failure/rejection occurs, the node shuts down immediately.

### Error modes and edge cases handled

- Action server not ready: The timer prints a waiting message and retries until available.
- Rejection: Logs a warning and stops; no retry loop by default (keeps behavior predictable).
- Invalid frames or TF issues: Out of scope for this node; Nav2 will report transform/navigation errors.
- Unreachable goals: The result will reflect failure; the node still exits cleanly.

## Launch design

File: `launch/send_goal.launch.py`

- Exposes launch arguments (`goal_x`, `goal_y`, `goal_yaw`, `frame_id`, `goals_yaml`, `halt_on_failure`) that map to node parameters, allowing:
  - CLI overrides (`ros2 launch ... goal_x:=2.0 ...`)
  - Reuse in higher-level launch descriptions.
- Runs the console script `send_goal` from the installed package to avoid hardcoding module paths.
- `output='screen'` for straightforward visibility of feedback and result.

### YAML goals support

- YAML schema (minimal):

  ```yaml
  goals:
    - { x: 2.0, y: 1.0, yaw: 1.57, frame_id: map }
    - { x: 0.0, y: 0.0, yaw: 0.0 }  # frame_id defaults to node parameter
  ```

- Validation: Non-dict entries or goals missing required numeric fields are skipped with warnings.
- Time semantics: Each goal uses the current node clock time for its header stamp at send time.
- Server readiness: The same timer-based wait is used before the first goal is sent.

## Packaging details and rationale

- `setup.py`:
  - `entry_points.console_scripts`: registers `send_goal` so `ros2 run nav2_goal_publisher send_goal` works.
  - `data_files`: installs `package.xml` and the `launch/` file under the share directory so the launch file is discoverable.
  - Removed deprecated `tests_require` (newer setuptools warns and ignores it).
- `setup.cfg`:
  - Ensures console scripts install into `$base/lib/<package>` which is what ROS 2 expects.
- `resource/nav2_goal_publisher`:
  - Required by ament to index the package (without it, tools won’t discover the package properly).
- `package.xml`:
  - Declares `ament_python` build type (Python-only) and the needed runtime dependencies.

## Contract summary (inputs/outputs)

- Inputs:
  - Parameters: `goal_x`, `goal_y`, `goal_yaw` (rad), `frame_id` (string), `auto_send` (bool), `goals_yaml` (string path), `halt_on_failure` (bool)
  - Nav2 stack must be running and providing the `navigate_to_pose` action server.
- Outputs:
  - Single-goal mode: sends one `NavigateToPose` goal and exits.
  - YAML mode: sends N goals in order; exits after the last goal or immediately on failure if `halt_on_failure=true`.
- Success criteria:
  - Goal is accepted; node reports result (success/failure) and shuts down cleanly.

## Extensibility

- Goal lists / waypoints: Extend the node to iterate a list of goals (YAML or parameter array) and send sequentially.
- Degrees support: Add a `goal_yaw_deg` parameter and mutually exclusive logic with `goal_yaw`.
- Orientation overrides: Allow passing a full quaternion, with validation.
- Timeouts/retries: Add parameters for server wait timeout and goal retry behavior.
- Namespacing: Support `--ros-args --remap navigate_to_pose:=<ns>/navigate_to_pose` for multi-robot setups.

## Testing strategy (suggested)

- Unit: Factor quaternion computation into a helper and test for a few yaw angles.
- Integration: In simulation (Gazebo/Nav2 bringup), assert the action is accepted and completes for a reachable waypoint.
- Static: `flake8`/`ruff` for style; minimal effort given the small footprint.

## Operational notes

- Performance: Negligible CPU/memory overhead; the node runs briefly and exits.
- Logging: Defaults to info-level; change to debug for verbose feedback.
- Security: No external network access; relies on ROS graph connectivity.

## Alternatives considered

- `ros2 action send_goal` CLI: Great for manual use, but launch/parameter integration and composability are limited.
- `nav2_simple_commander` (Python API): Higher-level convenience, but adds an extra dependency and is less instructive for showing the core action client pattern.
- C++ (`rclcpp`): Fine for larger systems, but increases complexity for this simple use case.

## Quick usage

See `README.md` for build/run examples. Typical launch:

```bash
ros2 launch nav2_goal_publisher send_goal.launch.py \
  goal_x:=2.0 goal_y:=1.0 goal_yaw:=1.57 frame_id:=map
```
