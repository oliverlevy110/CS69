#!/usr/bin/python

import rospy
from levy_cs69_a2.msg import Signal
from levy_cs69_a2.robot import Robot

def spin(f):
    r = rospy.Rate(2)
    while not rospy.is_shutdown():
        if f.mode == 'r':
            f.seek(0)
            contents = f.read()

            lines = contents.split("\n")
            words = lines[2].split(" ")
            
            strength = words[6]
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

    robot = Robot()
    robot.spin()

    spin(f)

