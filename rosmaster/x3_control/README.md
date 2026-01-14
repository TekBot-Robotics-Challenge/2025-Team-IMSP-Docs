# x3_control — QR scan service (added)

This package contains joystick teleop nodes and a QR scan service node.

## QR scanning node
- Script: `x3_control/scripts/qr_service_node.py`
- Service: `/scan_qr` (std_srvs/Trigger)
- Parameters (see `config/qr_params.yaml`):
  - `camera_index` (int)
  - `show_window` (bool)
  - `quartiers_file` (string)

## Quick start
1. Install Python dependencies (system/pip):

   pip3 install opencv-python numpy pyzbar pyyaml

2. Build and source your workspace:

   colcon build --packages-select x3_control
   source install/setup.bash

3. Launch the QR node:

   ros2 launch x3_control qr_scan_launch.py

4. Call the service:

   ros2 service call /scan_qr std_srvs/srv/Trigger "{}"


## Notes
- The node writes QR contents into `quartiers.yml` in the working directory.
- If you want joystick-to-scan integration I can add a sample parameterized mapping
  to `yahboom_joy_X3.py` (L2 behavior) and a launch that starts both nodes.
