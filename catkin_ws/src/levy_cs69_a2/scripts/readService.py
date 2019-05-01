#!/usr/bin/python

import time
import rospy
from levy_cs69_a2.msg import Signal
from levy_cs69_a2.srv import FindSignalStrength

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
        time_end = time.time() + 5
        #for averaging signal strength
        num_messages=0
        total_str=0.0

        while time.time()<time_end:
           num_messages += 1
           total_str += self.current_strength 
           
        rospy.loginfo("*************** IN READSERVICE **************\n signal average= %f \n", total_str/num_messages)
        value = total_str/num_messages
        return value


    def spin(self):
        rospy.spin()

if __name__ == "__main__":
    rospy.init_node("readStrength")
    read=Read()
    read.spin()
