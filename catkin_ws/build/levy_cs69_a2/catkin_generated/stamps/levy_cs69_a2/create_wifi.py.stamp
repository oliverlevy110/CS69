#!/usr/bin/python
import tf
import math
import rospy
from levy_cs69_a2.msg import Signal
from nav_msgs.msg import Odometry
from levy_cs69_a2.robot import Robot

class CreateWifi:
    def __init__(self):
        self.sub_strength = rospy.Subscriber("/odom",Odometry,self.position)
        self.pub = rospy.Publisher("/turtle/signal_strength", Signal, queue_size=5) 
        self.strength=0
        self.pos = [9,9]
             
    def spin(self):    
        r = rospy.Rate(5)
        while not rospy.is_shutdown():
            message = Signal()
            message.timestamp = rospy.get_rostime()
            message.frame_id = "2"
            ros.loginfo("IN CREATE_WIFI, signal strength = %f \n", self.strength)
            message.signal_strength = self.strength 
            self.pub.publish(message)
            r.sleep()

    def position(self,odometry_msg):
        pose = odometry_msg.pose.pose

        x=pose.position.x
        y=pose.position.y
        
        dist = math.sqrt((x-self.pos[0])**2+(y-self.pos[1])**2)
        
        rate = dist/2
        if dist<=2:
            self.strength=0
        else:
            self.strength = (rate**2)/100


if __name__ == "__main__":
    rospy.init_node("create_wifi")
    rospy.loginfo("create NODE IS INIT \n")
    createwifi = CreateWifi()
#    robot = Robot()
#    robot.spin()
#    rospy.loginfo("robot spin called \n")
    createwifi.spin()
    rospy.spin()

