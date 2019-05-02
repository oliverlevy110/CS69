#!/usr/bin/python
import tf
import math
import rospy
from levy_cs69_a2.msg import Signal
from nav_msgs.msg import Odometry
from levy_cs69_a2.robot import Robot
"""
Class that mimics a wifi signal by publishing a strength value based on the robot's position from the "center". 
Path loss based on Free Space Path Model.

"""
class CreateWifi:
    def __init__(self):

        #Subscribers and Publishers
        self.sub_strength = rospy.Subscriber("/odom",Odometry,self.position)
        self.pub = rospy.Publisher("/turtle/signal_strength", Signal, queue_size=5) 

        #Current Strength of Signal
        self.strength = 0
        
        #Center 
        self.pos = [9,9]
    
    """
    Continually send messages
    """         
    def spin(self):    
        r = rospy.Rate(5)
        while not rospy.is_shutdown():
            #Build message
            message = Signal()
            message.timestamp = rospy.get_rostime()
            message.frame_id = "2"
            message.signal_strength = self.strength 
            #Publish message
            self.pub.publish(message)
            r.sleep()

    """
    Update signal strength based on robot's position
    """
    def position(self,odometry_msg):
        pose = odometry_msg.pose.pose

        x=pose.position.x
        y=pose.position.y
        
        dist = math.sqrt((x-self.pos[0])**2+(y-self.pos[1])**2)

        # Free Space Path Loss
        deb0 = 20*math.log10(0.001 * 0.1) + 20*math.log10(1000 * 2.4) + 32.44 
        # Free Space Path Loss assuming dist in meters and frequency in MHz 
        deb = 20*math.log10(0.001 * dist) + 20*math.log10(1000 * 2.4) + 32.44 
        self.strength = -deb/deb0 * 10

"""
Launch CreateWifi Class
"""
if __name__ == "__main__":
    rospy.init_node("create_wifi")
    rospy.loginfo("create NODE IS INIT \n")
    createwifi = CreateWifi()
    createwifi.spin()
    rospy.spin()

