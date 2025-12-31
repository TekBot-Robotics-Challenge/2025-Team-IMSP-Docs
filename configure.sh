#!/usr/bin/env bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
mkdir -p ~/trc_ws/src
ln -s -t ~/trc_ws/src $SCRIPTPATH
cd ~/trc_ws

BIN_FOLDER=~/trc_ws/src/bin
if [ -d "$BIN_FOLDER" ]; then
    echo "Removing unnecessary bin folder: $BIN_FOLDER"
    rm -rf "$BIN_FOLDER"
fi

# sudo apt install ros-humble-turtlesim
sudo apt install ros-humble-image-publisher
sudo apt install ros-humble-robot-localization
sudo apt install ros-humble-imu-filter-madgwick

source /opt/ros/humble/setup.bash
colcon build --packages-select astra_camera astra_camera_msgs rplidar_ros yahboomcar_bringup yahboomcar_base_node --cmake-args -DCMAKE_CXX_FLAGS="-w" -Wno-dev
colcon build
source ~/trc_ws/install/setup.bash
