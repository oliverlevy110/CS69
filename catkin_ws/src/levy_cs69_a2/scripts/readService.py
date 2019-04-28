#!/usr/bin/python

import time
import rospy
from levy_cs69_a2.msg import Signal
from levy_cs69_a2.srv import FindSignalStrength

class Read:

    def __init__(self):   
        #current strength value
        self.current_strength; 
        #Subscribers
        sub_strength = rospy.Subscriber("/turtle/signal_strength", Signal, read_strength)
        #Publishers
        sub_service = rospy.Service("findSignalStrength", FindSignalStrength, processCall)


    """
    Continually read the current strength from the subscriber. 
    """
    def read_strength(self, message):
        self.cur_strength = signal_msg.signal_strength

    """
    Take the average wifi strength over 15 seconds
    """
    def processCall(self, rqst):
        #stop loop after 15 seconds
        time_end = time.time() + 15
        #for averaging signal strength
        num_messages=0
        total_str=0.0

        while time.time()<time_end:
           num_messages++
           total_str += self.cur_strength 
        
        return total_str/num_messages

if __name__ == "__main__":
    rospy.init_node("readStrength")
    read=Read()
    rospy.spin()
