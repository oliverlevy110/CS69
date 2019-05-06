#!/usr/bin/python

import rospy
from levy_cs69_a2.msg import Signal
from levy_cs69_a2.robot import Robot

"""
Read wifi strength from /proc/net/wireless and publish to /turtle/signal_strength topic
"""
def spin(f):
    r = rospy.Rate(2)
    while not rospy.is_shutdown():
        #read file
        if f.mode == 'r':
            #start from beginning of file
            f.seek(0)
            contents = f.read()

            lines = contents.split("\n")
            words = lines[2].split(" ")
            
            strength = words[6]

            #build message
            message = Signal()
            message.timestamp = rospy.get_rostime()
            message.frame_id = "2"
            message.signal_strength = float(strength) 
            pub.publish(message)
        r.sleep()    

if __name__ == "__main__":
    rospy.init_node("follow_wifi")
    pub = rospy.Publisher("signal_strength", Signal, queue_size=5) 
    f=open("/proc/net/wireless","r")

    spin(f)

