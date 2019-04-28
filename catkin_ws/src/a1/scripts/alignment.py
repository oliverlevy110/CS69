#!/usr/bin/python

import rospy
import numpy
import tf
import math
from geometry_msgs.msg import Twist, Pose, Point 
from nav_msgs.msg import Odometry

"""
import imp

f, filename, desc = imp.find_module('robot', ['/home/oliverlevyorl/CS69/catkin_ws/src/a1/src/robot.py'])
robot_var = imp.load_module('robot', f, filename, desc)
"""

from a1.robot import Robot

class alignment:

	def __init__(self):
	
		self.heading= Point(0,0,0)

		self.pub= rospy.Publisher('heading_point', Point, queue_size=3)
		
		self.sub=[]
		for i in range(0,2):
			sub.append(rospy.Subscriber("/robot_"+str(i)+"/base_pose_ground_truth", Odometry , new_heading))
	
		robot = Robot();
		robot.spin();
		rospy.spin();
	
	def new_heading(self, bpgt):
		cur_heading = self.heading
		pub = self.pub

		x = bpgt.pose.pose.position.x 
		y = bpgt.pose.pose.position.y
	
		quaternion = (
	        	bpgt.pose.pose.orientation.x,
	        	bpgt.pose.pose.orientation.y,
	        	bpgt.pose.pose.orientation.z,
	        	bpgt.pose.pose.orientation.w)
        
		euler = tf.transformations.euler_from_quaternion(quaternion)
	    	theta = euler[2]
	
		new_x= x + 5*math.sin(theta)
		new_y= y + 5*math.cos(theta) 	
	

		point = Point()
		point.x = cur_heading.x + (cur_heading.x - (0.1*new_x))
		point.y= cur_heading.y + (cur_heading.y - (0.1*new_y))
		point.z = 0

		pub.publish(point)
		
		self.heading.x = point.x
		self.heading.y = point.y

if __name__=="__main__":
	rospy.init_node("alignment")
	al = alignment()




