# Oliver Levy
# Professor Li
# Flocking behavior on ROS for COSC69/169 Multirobot systems

### Starting the Program
Go into the flocking folder and run:

```
roslaunch flocking simulation.launch
```

Stage will popup with 10 robots on a map. To close, exit stage or ctrl-C the program.

### How it runs
The simulation launch file will start and create the stageros node. It will then subsequently create 10 robots and call robot.launch.
Robot.launch will call `start_node.py` for each robot. The `start_node` will start robot.py, which then controls the robot's velocity in Stage.

