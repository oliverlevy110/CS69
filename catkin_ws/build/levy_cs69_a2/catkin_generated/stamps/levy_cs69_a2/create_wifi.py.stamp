
#!/usr/bin/python

import math
import rospy
from levy_cs69_a2.msg import Signal


class CreateWifi:
    def __init__(self):
        self.sub_strength = rospy.Subscriber("odom",Odom,position)
        self.pub = rospy.Publisher("signal_strength", Signal, queue_size=5) 
        self.strength
        self.pos = [5,5]
             
    def spin():    
        r = rospy.Rate(5);
        while not rospy.is_shutdown():
            message = Signal()
            message.timestamp = rospy.get_rostime()
            message.frame_id = "2"
            message.signal_strength = self.strength 
            pub.publish(message)
            r.sleep()

    def position(self,odom):
        pose = odometry_msg.pose.pose

        x=pose.position.x
        y=pose.position.y
        
        dist = math.sqrt((x-pos[0])**2+(y-pos[1])**2)
        
        rate = dist/2
        if dist<=2:
            self.strength=0
        else
            self.strength = -1/(rate**2)


if __name__ == "__main__":
    rospy.init_node("create_wifi")
    createwifi = CreateWifi()
    createwifi.spin()


