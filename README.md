
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
