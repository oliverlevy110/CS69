#!/usr/bin/python

import time
import rospy
from levy_cs69_a2.msg import Signal
from levy_cs69_a2.srv import FindSignalStrength

"""
Read the wifi signal from /turtle/signal_strength topic
When receive a call from Robot(), average the signal strengths over 5 seconds and return the value

"""
class Read:

    def __init__(self):   
        #current strength value
        self.current_strength=0; 
        #Subscribers
        self.sub_strength = rospy.Subscriber("/turtle/signal_strength", Signal, self.read_strength)
        #Publishers
        self.sub_service = rospy.Service("findSignalStrength", FindSignalStrength, self.processCall)


    """
    Continually read the current strength from the subscriber. 
    """
    def read_strength(self, message):
        self.current_strength = message.signal_strength

    """
    Take the average wifi strength over 15 seconds
    """
    def processCall(self, rqst):
        #stop loop after 5 seconds
        go = rospy.get_rostime()
        stop = go + rospy.Duration(5) 
        #for averaging signal strength
        num_messages=0
        total_str=0.0

        while go<stop:
           go = rospy.get_rostime()
           num_messages += 1
           total_str += self.current_strength 
           
        value = total_str/num_messages
        return value


    def spin(self):
        rospy.spin()

if __name__ == "__main__":
    rospy.init_node("readStrength")
    read=Read()
    read.spin()
