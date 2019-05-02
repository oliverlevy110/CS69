#!/usr/bin/python

import tf
import math
import numpy
import rospy
import time

from threading import Thread
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from levy_cs69_a2.srv import FindSignalStrength
from levy_cs69_a2.triangulateCalculation import TriangulateCalculation
from levy_cs69_a2.msg import Signal

"""
Class to control robot behavior.

Input: signal strength to stop at. 

Behaviors are broken into two sections. Each section operates its behaviors on its own thread.

    - Callbacks update instance variables. The safety callback also controls reactive obstacle avoidance.
        - Update position
        - Update strength of wifi signal
        - Avoid obstacles during all phases except triangulation
 
    - Controlling behaviors use instance variables to make decision on robot's movement.
        - Main controller to keep track of time and calls to following behaviors. 
        - Triangulate (visit three points and call service to average strengths)
        - Find and go to signal source as determined by CalculateTriangulation class
        - Check robot's straight line path for obstacles before moving
            - Predictive obstacle avoidance during triangulation

Obstacle Avoidance is split among 2 functions:
    - First is safety_callback: reacts to objects within a defined danger zone. 
    - Second is clear: looks for objects in front of robot. Shortens the distance for the robot to travel
                        if there is an object in front of it. Only is called during triangulation.
"""


class Robot:
    def __init__(self, strength = -40):
        #subscribers
        self.sub_strength = rospy.Subscriber("/odom",Odometry,self.find_position)
        self.safety_call = rospy.Subscriber("/base_scan", LaserScan, self.safety_callback, queue_size=1)
        self.sub_strength = rospy.Subscriber("/turtle/signal_strength", Signal, self.read_strength)

        #publishers and publishing rate
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=5)        
        self.pub_rate = 5

        #Service Proxies
        self.triangulate = rospy.ServiceProxy("findSignalStrength", FindSignalStrength)

        #data used for triangulating
        self.strengths={}

        #error margin
        self.error = 0.05
        
        #controls angle that the robot reads obstacles
        self.divide = 6        

        #robot's current position: x,y,yaw
        self.position=[0,0,0]

        #booleans that tell if have a position and a goal point
        self.has_position = False    
        self.has_goal = False

        #Robot's current velocity
        self.cmd_msg = Twist()

        #time between triangulation iterations 
        self.time_btw = 25      

        #Goal to get to: x,y
        self.goal=[0,0]
    
        #control booleans
        self.triangulate_control = False
        self.safety_control = False
        self.have_safety_message = False

        #triangulate distance and angles
        self.triangulate_dist = 2
        self.triangulate_angle = 2.09 

        # current signal strength
        self.current_strength = 0

        # safety control variables
        self.danger = 0.5
        self.stop = strength
        self.msg = LaserScan() 

##################### Callbacks  #######################
    """
    Find the robot's current position and save it to self.position
    Turn self.has_position to true - indicating that other programs that rely on this information can start
    """
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

    """
    Detect if there are objects in front of the robot.
    If so, calculate the angle to avoid them.
    Let the robot continue straight for several seconds 
    """
    def safety_callback(self, laser_scan_msg):
        #get the range of angles that the robot sees.
        ranges = numpy.array(laser_scan_msg.ranges)

        #indicates to clear() that it can assess data from self.msg
        self.have_safety_message = True
        self.msg= laser_scan_msg
        
        #get the minimum angle and angle increment
        angle_min = laser_scan_msg.angle_min
        angle_inc = laser_scan_msg.angle_increment

        #position in array
        pos = 0

        # bounding angles to for objects in. Equal to -pi/x and pi/x. Transforms these into positions in the array for reference.
        pos_neg_Halfpi = ((-math.pi/self.divide)- angle_min)/angle_inc
        pos_Halfpi = ((math.pi/self.divide)- angle_min)/angle_inc


        # search through all the ranges. If any are less than self.danger and are within pi/x and -pi/x, angle the robot away from the object
        break_bool = False
        for dist in ranges:
            if(dist<self.danger and not break_bool):
                if (pos>pos_neg_Halfpi and pos<pos_Halfpi):
                    #block other programs that influence velocity commands from starting
                    self.safety_control = True
                    # if the value is within bounding angles, calculate the angle by which to avoid the object
                    if (abs(pos - pos_neg_Halfpi) < abs(pos-pos_Halfpi)):
                        step = pos_neg_Halfpi+pos 
                        angle = (step * angle_inc) + angle_min + math.pi/self.divide

                    else:
                        step = pos - pos_Halfpi
                        angle = (step * angle_inc) + angle_min - math.pi/self.divide

                    #turn based on angle calculated 
                    self.cmd_msg.linear.x = 0
                    self.cmd_msg.angular.z = angle
                    time.sleep(1)
                    self.cmd_msg.angular.z = 0
                    # go forward away from object
                    self.cmd_msg.linear.x = 0.22
                    time.sleep(2)
                    self.safety_control=False
                    break_bool=True
            
            pos += 1
 
    """
    Update the signal strength value
    """
    def read_strength(self, message):
        self.current_strength = message.signal_strength

################## Controlling Behaviors #########################

    """
    Check for objects in front of robot before moving. Works very similarly to safety_callback
    """
    def clear(self):
        while(not self.have_safety_message):
            time.sleep(0.5) 
        time.sleep(1)
        ranges = numpy.array(self.msg.ranges)
        angle_min = self.msg.angle_min
        angle_inc = self.msg.angle_increment

        pos_neg_Halfpi = ((-math.pi/self.divide)- angle_min)/angle_inc
        pos_Halfpi = ((math.pi/self.divide)- angle_min)/angle_inc
        pos = 0
        for dist in ranges:
            if(dist<self.triangulate_dist):
                # if the object is within the bounding angle range, send a distance that stops the robot short of the object
                if (pos>pos_neg_Halfpi and pos<pos_Halfpi):
                    return dist-1.00
            pos += 1
        #otherwise, go the full triangulation distance as specified by self.triangulate_dist
        return self.triangulate_dist
        
    """
    Starting Conditions:
        - the robot does not currently have a goal
        - the robot is not currently running triangulation
        - the robot is not avoiding obstacles
    
    Find the source of the signal by calling triangulate from TriangulationCalculation class

    Calculate the angle to the goal and turn the robot.

    Go forward.

    Update has_goal, indicating the robot has a goal 
    """
    def find_goal(self):
        if self.safety_control == False and self.triangulate_control == False and self.has_goal == False:
            # find source
            find = TriangulateCalculation()
            intermediary = find.triangulate(self.strengths, self.error)
            
            # reset strengths variable
            self.strengths = {}

            # if the function calculated a valid goal point, put it into self.goal
            if(intermediary[0] != 0): 
                self.goal = intermediary
            else:
                rospy.loginfo("Unable to read goal point.\n")
            
            rospy.loginfo("Goal Point: %f,%f\n", self.goal[0], self.goal[1])

            #calculate the angle between the robot and the goal
            theta = math.atan2(self.goal[1]-self.position[1], self.goal[0]-self.position[0])
            sum_theta_x = math.cos(theta)+math.cos(self.position[2]) 
            sum_theta_y = math.sin(theta)+math.sin(self.position[2]) 
            new_theta = math.atan2(sum_theta_y, sum_theta_x) 
            
            rospy.loginfo("theta: %f, pos: %f, angle of vector pos: %f, angle of goal: %f , new_theta = %f",theta, self.position[2], math.atan2(self.position[1],self.position[0]),math.atan2(self.goal[1], self.goal[0]),new_theta)

            # Turn the robot towards the goal
            time_ang = new_theta
            if time_ang >0:
                self.cmd_msg.angular.z = 1.0
            else:
                self.cmd_msg.angular.z = -1.0

            time.sleep(abs(float(time_ang)))
            self.cmd_msg.angular.z = 0

            # move the robot forward
            dist = math.sqrt((self.position[0]- self.goal[0])**2 + (self.position[1] - self.goal[1])**2 )
            self.cmd_msg.linear.x = 0.22
            self.has_goal = True


    """
    Steer the robot at an angle and distance to collect data on signal strength
    """
    def start_triangulate(self):
        if self.safety_control == False:
            
            #turn the robot
            self.cmd_msg.angular.z = 1.0 
            time.sleep(abs(self.triangulate_angle))
            self.cmd_msg.angular.z = 0
    
            #move the robot forward self.triangulate_dist or the distance available to it
            can_travel =abs(self.clear())
            self.cmd_msg.linear.x = 0.22
            time_travel = can_travel/0.22
            time.sleep(time_travel)
            self.cmd_msg.linear.x = 0

            #call the service to calculate the average signal strength at a point
            try:
                strengthResponce = self.triangulate(0,0,0)
                strength = strengthResponce.avg_str
            except:
                rospy.loginfo("Error communicating with the server \n")
                strength = 0

            rospy.loginfo("Strength: %f \n Position: %f,%f", strength, self.position[0], self.position[1])

            #update the dictionary mapping strengths to position
            self.strengths[strength] = [self.position[0], self.position[1]]

            #reset the robot goal indicator
            self.has_goal = False 

    """
    Main Controller for controlling behaviors. Governs the periodic function calls to triangualtion and find_goal
    """

    def triangulationController(self):
        goalbool = False 
        time_end = time.time() + self.time_btw
        while not rospy.is_shutdown():
            #every self.time_btw seconds, triangulate
            if(((time.time()-time_end)%self.time_btw) < 0.4):
                self.triangulate_control = True
                self.start_triangulate()
                self.start_triangulate()
                self.start_triangulate()

                self.triangulate_control = False
                goalbool = True
            elif goalbool and self.has_goal == False:
                
                self.find_goal()
                time_end = time.time() + self.time_btw
            else: 
                pass

            time.sleep(1)
            
####################### Spin ##############################

    def spin(self):
        r = rospy.Rate(self.pub_rate)
        startbool = True
        rospy.wait_for_service('findSignalStrength')
        while not rospy.is_shutdown():

            #if not started, make a new thread for starting the control behaviors
            if(self.has_position and startbool): 
                thread = Thread(target = self.triangulationController)
                thread.start()
                startbool=False

            #quit controlling the robot if you have reach the signal strength desired
            if(self.current_strength>=self.stop and self.current_strength<0):
                thread.join()
                rospy.loginfo("STOPPED \n")
                self.cmd_msg.linear.x = 0
                self.cmd_msg.angular.z = 0
            #publish velocity messages
            self.pub.publish(self.cmd_msg)
            r.sleep()



