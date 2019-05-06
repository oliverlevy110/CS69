# Oliver Levy
# Professor Quattrini Li
# COSC69/169 Multirobot systems
# Wifi Tracking behavior on ROS 

### Simulation
#### Starting the Program

Go into the `levy_cs69_a2` folder. 

Then run:

```
roslaunch `levy_cs69_a2` simulation.launch
```
To provide a strength argument, run:

```
roslaunch `levy_cs69_a2` simulation.launch:=x
```
where `x` is the desired value. Stage will popup with 1 robot on a map. To close, ctrl-C the program.

#### How it runs
The simulation launch file will start and create the stageros node. It will then create a robot and call robot.launch.
Robot.launch will call `start_node.py`, `create_wifi.py` and `readService.py`. The `start_node` will start robot.py, which then controls the robot's velocity in Stage. `create_wifi` controls the value of the wifi signal, and `readService.py` averages the signal produced by `create_wifi.py`

### On the Robot

SSH into the robot. Go into the `catkin_ws/src/levy_cs69_a2` folder.
Follow Professor Quattrini Li's instructions to bring up the robot. When ready, run:

```
roslaunch `levy_cs69_a2` `levy_cs69_a2_robot.launch`
```

#### How it runs

The launch file will call `start_node.py`, `follow_wifi.py` and `readService.py`. The `start_node` will start robot.py, which then controls the robot's velocity in Stage. `follow_wifi` reads the value of the wifi signal, and `readService.py` averages the signal read by `follow_wifi.py`when called.


