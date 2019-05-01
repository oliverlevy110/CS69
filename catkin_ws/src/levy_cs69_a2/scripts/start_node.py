#!/usr/bin/python

from levy_cs69_a2.robot import Robot
import rospy
if __name__ == "__main__":
    rospy.init_node("start_node")
    strength = rospy.get_param("strength") 
    rospy.loginfo("strength = %f]n", strength)
    robot = Robot(strength)
    robot.spin()

