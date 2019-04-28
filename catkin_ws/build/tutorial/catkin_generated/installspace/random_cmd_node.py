#!/usr/bin/python

from numpy.random import seed

from tutorial.robot import Robot

import rospy

if __name__ == "__main__":
    rospy.init_node("random_cmd")
    seed_value = rospy.get_param("~seed_value", 0)

    rospy.loginfo("seed_value={}".format(seed_value))

    seed(seed_value)

    robot = Robot()
    robot.spin()

