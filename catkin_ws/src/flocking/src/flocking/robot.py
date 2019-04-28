from numpy.random import rand
from random import *
from geometry_msgs.msg import Twist, Pose, Point
from nav_msgs.msg import Odometry 
from std_srvs.srv import Trigger
from std_srvs.srv import TriggerResponse
from sensor_msgs.msg import LaserScan

import tf
import rospy
import numpy
import math

class Robot:
    """Robot class for controlling its behavior.
    Attributes:
        safety (bool): a bool on whether the robot is too close to an object or not
        danger (float): the distance from an object at which the robot needs to keep
        x,y,theta (float): descriptors of the robots current position in space
        heading_point (Point): the point for the robot to follow
        cmd_pub (:obj:Publisher): publisher for command velocities.
        cmd_msg (Twist): the velocity message to send to cmd_pub
        sub, sub_me, safety_call (Subscriber): subscribers for base_pose_ground_truth and base_scan information
        
        sub is a list of Subscribers for all robots, while sub_me is a subscriber for the robot in this program's namespace only. 
    """
    def __init__(self, frequency=1):
        """Constructor.
        Args:
            frequency (int, optional): frequency frequency rate for sending commands to the robot.
        """
        self.frequency = frequency
        

        self.x = 0
        self.y = 0 
        self.theta = 0        
        self.heading_point = Point()

        self.safety = False
        self.danger = 0.75 

        
        self.cmd_msg = Twist()
        self.pose = {}
        self.cmd_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
        self.sub=[]

        #Publishers and Subscribers 
        for i in range(0,10):
            self.sub.append(rospy.Subscriber("/robot_"+str(i)+"/base_pose_ground_truth", Odometry , self.heading, callback_args=(i)))
        self.sub_me = rospy.Subscriber("base_pose_ground_truth", Odometry, self.find_trajectory)
        self.safety_call = rospy.Subscriber("base_scan", LaserScan, self.safety_callback)

    """
    Arguments: Odometry message from Subscriber Object
 
    Given the position for robot i, this function updates the dictionary of robot positions,
    calculates the new average position of the robots, and stores it in self.heading. """
    def heading(self, bpgt, args):
        # find robot's position
        robot_i = args
        
        x = bpgt.pose.pose.position.x 
        y = bpgt.pose.pose.position.y
	
        quaternion = (
            bpgt.pose.pose.orientation.x,
            bpgt.pose.pose.orientation.y,
            bpgt.pose.pose.orientation.z,
            bpgt.pose.pose.orientation.w)
        
        euler = tf.transformations.euler_from_quaternion(quaternion)
        theta = euler[2]
        
        #update dictionary

        self.pose[robot_i] = [x,y,theta]
        avg_pose = self.find_average(self.pose)
    
        # determine heading point
        self.heading_point.x = avg_pose[0] + 4*math.cos(avg_pose[2])
        self.heading_point.y = avg_pose[1] + 4*math.sin(avg_pose[2])
        self.heading_point.z = 0 	


    """
    Arguments: Position of robot of the namespace that this node is in.

    Given an odometry message, determine the robot's position and calculate a trajectory towards the heading point.
    Update the cmd_msg with that trajectory.  
    If safety attribute is True, instead rotate.  
    """
    def find_trajectory(self, bpgt):
        # find robot's position
        self.x = bpgt.pose.pose.position.x 
        self.y = bpgt.pose.pose.position.y
            
        quaternion = (
            bpgt.pose.pose.orientation.x,
            bpgt.pose.pose.orientation.y,
            bpgt.pose.pose.orientation.z,
            bpgt.pose.pose.orientation.w)
                
        euler = tf.transformations.euler_from_quaternion(quaternion)
        self.theta = euler[2]

        #determine distance and angle to target
        delta_x = self.heading_point.x - self.x 
        delta_y = self.heading_point.y - self.y  
        
        theta_g = math.atan2(delta_y,delta_x)-self.theta
        dist = math.sqrt((delta_x)**2 + (delta_y)**2)
            
        # determine linear and angular velocity

        lin_vel = dist/2
        ang_vel = theta_g/2

        #update velocity message
        if (not self.safety): 
            self.cmd_msg.linear.x = lin_vel
            self.cmd_msg.angular.z = ang_vel
        else:
            self.cmd_msg.linear.x = 0
            self.cmd_msg.angular.z = 0.5

    """
    Arguments: Dictionary of robot positions.

    Given the dictionary of robot locations, calculate the average point among them."""
    def find_average(self, pose):
        
        sum_x=0.0
        sum_y=0.0
        sum_theta_x=0.0
        sum_theta_y = 0.0
        sum_theta=0.0
        num = 0

        for value in pose.values():
            delta_x = value[0] - self.x 
            delta_y = value[1] - self.y  
            dist = math.sqrt((delta_x)**2 + (delta_y)**2)
            if (dist<6):
                sum_x += value[0]
                sum_y += value[1]

                #sum the cartesian coordinates of the angles
                sum_theta_x += math.cos(value[2])
                sum_theta_y += math.sin(value[2])
                num += 1
        
        #find the average angle
        sum_theta = math.atan2(sum_theta_y, sum_theta_x)

        if (num>0):
            pose_list=[sum_x/num, sum_y/num, sum_theta]
        else:
            pose_list=[sum_x, sum_y, sum_theta]
        return pose_list


    """
    Spin function. Publishes cmd_msg to cmd_vel
    """
    def spin(self):
        r = rospy.Rate(2)
        while not rospy.is_shutdown():        
            self.cmd_pub.publish(self.cmd_msg)
            r.sleep() 
      

    """
    Arguments: Laser Scan from Base_scan topic

    This function determines if the robot has any objects in front of it within one meter.
    """       
    def safety_callback(self, laser_scan_msg):
        #get the range of angles that the robot sees.
        ranges = numpy.array(laser_scan_msg.ranges)

        min_reading =[] #5.0
        min_pos=[] #0        
        pos = 0

        # search through all the ranges. If any are less than self.danger and are within pi/2 or -pi/2, turn self.safety to True
        for dist in ranges:
            if(dist<self.danger and pos>179 and pos<527):#min_reading):
                self.safety = True
                break
            else:
                self.safety=False
            pos += 1
 
