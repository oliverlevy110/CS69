#!/usr/bin/python

import tf
import math
import rospy
import time

from threading import Thread
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from levy_cs69_a2.srv import FindSignalStrength
from levy_cs69_a2.triangulateCalculation import TriangulateCalculation

class Robot:
    # implement passing this parameter
    def __init__(self, strength = 40):
        #subscribers
        self.sub_strength = rospy.Subscriber("/odom",Odometry,self.find_position)
        #add subscriber to wifi strength, to slow robot if within strength range
        #add subscriber for laser scan
        #publishers and publishing rate
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=5)        
        self.pub_rate = 5

        #Service Proxies
        self.triangulate = rospy.ServiceProxy("findSignalStrength", FindSignalStrength)
        #data used for triangulating
        self.strengths={}

        #error margin
        self.error = 0.05
        
        
        #robot's current position
        #x,y,yaw
        self.position=[]
        self.has_position = False    

        #Robot's current velocity
        self.cmd_msg = Twist()
        
        #Goal to get to
        #x,y
        self.goal=[0,0]
    
        #control booleans
        self.triangulate_control = False
        self.safety_control = False

        #triangulate distance and angles
        self.triangulate_dist = 2
        self.triangulate_angle = 2.09 

##################### Callbacks  #######################

    def find_position(self, odometry_msg):
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
        self.has_position = True


    def safety(self):
        rospy.loginfo("You are in God's hands now my son.\n")


################## Controlling Behaviors #########################

    #steering to goal
    def find_goal(self):
        if self.safety_control == False and self.triangulate_control == False:
            find = TriangulateCalculation()
            intermediary = find.triangulate(self.strengths, self.error)
            if(intermediary[0] != 0): 
                self.goal = intermediary
            else:
                rospy.loginfo("Unable to read goal point.\n")
            
            rospy.loginfo("Goal Point: %f,%f\n", self.goal[0], self.goal[1])
            theta = math.atan2(self.goal[1]- self.position[1], self.goal[0] -self.position[0])
            sum_theta_x = math.cos(self.position[2]) + math.cos(theta)
            sum_theta_y = math.sin(self.position[2]) + math.sin(theta)
            new_theta = math.atan2(sum_theta_y, sum_theta_x) 
            
            time_ang = new_theta
            self.cmd_msg.angular.z = 1.0
            time.sleep(abs(float(time_ang)))
            self.cmd_msg.angular.z = 0


            dist = math.sqrt((self.position[0]- self.goal[0])**2 + (self.position[1] - self.goal[1])**2 )
            time_travel=dist/0.22
            self.cmd_msg.linear.x = 0.22
            time.sleep(time_travel)
            self.cmd_msg.linear.x = 0



    #triangulation steering    
    def start_triangulate(self):
        if self.safety_control == False:
                
            self.cmd_msg.angular.z = 1.0 
            time.sleep(abs(self.triangulate_angle))
            self.cmd_msg.angular.z = 0
 
            self.cmd_msg.linear.x = 0.22
            time_travel = self.triangulate_dist/0.22
            time.sleep(time_travel)
            self.cmd_msg.linear.x = 0

            try:
                strengthResponce = self.triangulate(0,0,0)
                strength = strengthResponce.avg_str
            except:
                rospy.loginfo("Error communicating with the server \n")
                strength = 0
            rospy.loginfo("Strength: %f \n Position: %f,%f", strength, self.position[0], self.position[1])
            self.strengths[strength] = [self.position[0], self.position[1]]
            


    def triangulationController(self):
        goalbool = False 
        time_end = time.time() + 10
        while True and not rospy.is_shutdown():

            if(((time.time()-time_end)%10) < 0.4):
                self.triangulate_control = True
                rospy.loginfo("\n TRIANGULATING \n")
                self.start_triangulate()
                self.start_triangulate()
                self.start_triangulate()

                self.triangulate_control = False
                goalbool = True
            elif goalbool:
                self.find_goal()
            else: 
                pass

            time.sleep(1)
            
####################### Spin ##############################

    def spin(self):
        r = rospy.Rate(self.pub_rate)
        startbool = True
        rospy.wait_for_service('findSignalStrength')
        while not rospy.is_shutdown():
            if(self.has_position and startbool): 
                thread = Thread(target = self.triangulationController)
                thread.start()
                startbool=False
            self.pub.publish(self.cmd_msg)
            r.sleep()



