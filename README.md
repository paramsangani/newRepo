
#TESTING

# Notes ROS 2 Node

```
cd PX4-Autopilot
make distclean
make clean
```

```
cd ../ws_ros2/
colcon build
```
If colcon build fails

```
source /opt/ros/humble/setup.bash
source ~/ws_ros2/install/setup.bash
```
## Build PX4 firmware for SITL, and run it
```
cd ~/PX4-Autopilot
make px4_sitl jmavsim
```
## Run the agent in another terminal
```
# micrortps_agent -t UDP
MicroXRCEAgent udp4 -p 8888
```
## Run the ROS 2 node in another terminal (offboard_control)
```
cd ~/ws_ros2
source install/local_setup.bash
ros2 run px4_ros_com offboard_control
```
