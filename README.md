
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
If colco build fails

```
source /opt/ros/humble/setup.bash
source ~/ws_ros2/install/setup.bash
```
```
micrortps_agent -t UDP
MicroXRCEAgent udp4 -p 8888
```
