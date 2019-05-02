#!/usr/bin/python

from levy_cs69_a2.robot import Robot
import rospy


"""
Initialize and start Robot() class
Pass it the strength parameter
"""
if __name__ == "__main__":
    rospy.init_node("start_node")
    strength = rospy.get_param("strength") 
    robot = Robot(strength)
    robot.spin()

