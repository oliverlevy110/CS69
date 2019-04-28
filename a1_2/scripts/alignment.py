#!/usr/bin/python

import rospy
import numpy
import tf
import math
from geometry_msgs.msg import Twist, Pose, Point 
from nav_msgs.msg import Odometry

# having problem resolving subscribing message type. Cant import odometry or cant recognize the name


def new_heading(bpgt, args):
	cur_heading=args[0]
	pub=args[1]

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


if __name__=="__main__":
	rospy.init_node("alignment")

 	heading= Point(0,0,0)

	pub= rospy.Publisher('heading_point', Point, queue_size=3)
	
	sub=[]
	for i in range(0,2):
		sub.append(rospy.Subscriber("/robot_"+str(i)+"/base_pose_ground_truth", Odometry , new_heading,  callback_args=(heading, pub)))
	rospy.spin();



