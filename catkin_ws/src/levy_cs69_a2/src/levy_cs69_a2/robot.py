#!/usr/bin/python

import math
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from levy_cs69_a2.triangulateCalculation import TriangulateCalculation

class Robot:
    # implement passing this parameter
    def __init__(self, strength = 40):
        #subscribers
        self.sub_strength = rospy.Subscriber("odom",Odom,self.find_position)
        #add subscriber to wifi strength, to slow robot if within strength range
        #add subscriber for laser scan
        #publishers and publishing rate
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=5)        
        self.pub_rate = 5;

        #Service Proxies
        self.triangulate = rospy.ServiceProxy("findSignalStrength", FindSignalStrength)

        #data used for triangulating
        self.strengths={}

        #error margin
        self.error = 0.2
        
        
        #robot's current position
        #x,y,yaw
        self.position;
    
        #Robot's current velocity
        self.cmd_msg = Twist();
        
        #Goal to get to
        #x,y
        self.goal;
    
        #control booleans
        self.triangulate_control = False
        self.safety_control = False


        #triangulate distance and angles
        self.triangulate_dist = 1
        self.triangulate_angle = 60
        self.triangulate_point;

##################### Current Position and Reading if arrived at Goals #######################

    def find_position(self, odom):
        pose = odometry_msg.pose.pose

        x=pose.position.x
        y=pose.position.y

        quaternion = (
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z,
            pose.orientation.w)
        euler = tf.transformations.euler_from_quaternion(quaternion)
        yaw = euler[2]

        self.position = [x,y,yaw]

    #goal is in the form x,y
    def read_goal(self,goal):
        if (   
                self.goal[0] - self.position[0] < self.error and
                self.goal[1] - self.position[1] < self.error
           ):   return True
        else: 
            return False 

################### Finding Goals #########################
    #done
    def find_tri_goal(self): 
        sum_theta_x = math.cos(self.position[2]) + math.cos(self.triangulate_angle)
        sum_theta_y = math.sin(self.position[2]) + math.sin(self.triangulate_angle)
        new_theta = math.atan2(sum_theta_y, sum_theta_x) 
        new_x = self.position[0] + math.cos(new_theta)
        new_y = self.position[1] + math.cos(new_theta)
        return [new_x,new_y,new_theta]

################## Steering Behaviors #########################

    #steering to goal
    def find_goal(self):
        if self.safety_control == False and self.triangulate_control == False:
            find = TriangulateCalculation()
            intermediary = find.triangulate(self.strengths, self.error)
            if(intermediary[0] != 0): 
                goal = intermediary;
            else:
                print("Unable to read goal point.\n")
            
            while self.read_goal(self.goal) != True:
                self.cmd_msg.linear.x = 0.22
                dist = math.sqrt((self.triangulate_point[0]- self.position[0])**2 + (self.triangulate_point[1]- self.position[1])**2 )
                ang_divide = dist/0.22

                theta = atan2(self.goal[1]- self.position[1], self.goal[0] -self.position[0])
                sum_theta_x = math.cos(self.position[2]) + math.cos(theta)
                sum_theta_y = math.sin(self.position[2]) + math.sin(theta)
                new_theta = math.atan2(sum_theta_y, sum_theta_x) 

                self.cmd_msg.angular.z = new_theta / ang_divide 

    #triangulation steering    
    def start_triangulate(self):
        self.triangulate_point = self.find_tri_goal() 
        if self.safety == False:
            while self.read_goal(self.triangulate_point) != True:
                dist = math.sqrt((self.triangulate_point[0]- self.position[0])**2 + (self.triangulate_point[1]- self.position[1])**2 )
                self.cmd_msg.linear.x = 0.22
                ang_divide = dist/0.22
                self.cmd_msg.angular.z = self.triangulate_angle / ang_divide
            self.cmd_msg.linear.x= 0
            self.cmd_msg.angular.z =0 
            rospy.wait_for_service('findSignalStrength')
            try:
                strength = self.triangulate(0,0,0)
            except:
                print("Error communicating with the server \n")
            
            


    def safety(self):
        print("You are in God's hands now my son.\n")

######################### Controllers and Spin ##############################3

    def triangulationController(self):
        self.triangulate_control = True;

        self.start_triangulate()
        self.start_triangulate()
        self.start_triangulate()

        self.triangulate_control = False;

    def spin(self):
        r = rospy.Rate(self.pub_rate)
        i = 0
        while not rospy.is_shutdown():
            
            self.pub.publish(self.cmd_msg)
            if i % 15*pub_rate:
                self.triangulationController()
            else:
                self.find_goal()
            r.sleep()



