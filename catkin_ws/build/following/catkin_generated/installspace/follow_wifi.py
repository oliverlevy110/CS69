#!/usr/bin/python

if __name__ == "main":
    rospy.init_node("follow_wifi")
    pub = rospy.Publisher("signal_strength", )


def spin():
    f=open("/proc/net/wireless","r")
    r = rospy.Rate(2)
    while not rospy.is_shutdown():
        if f.mode == 'r':
            contents = f.read()
            print contents
        r.sleep()    
