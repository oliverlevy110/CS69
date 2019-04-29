#!/usr/bin/python


import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan


class Robot:
    # implement passing this parameter
    def __init__(self, strength = 40):
        #subscribers
        self.sub_strength = rospy.Subscriber("some...",Odom,self.find_position)
        # add subscriber for laser scan
        #publishers 
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=5)        

        #data used for triangulating
        self.strengths={}

        #robot's current position
        self.position;
    
        #Goal to get to
        self.goal;
    
        #control booleans
        self.triangulate_control = False
        self.safety_control = False

        #triangulate distance and angles
        self.triangulate_dist = 2
        self.triangulate_angle = 60

    def find_position(self, odom):
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
            
        
    def start_triangulate(self):
        pass 

    def find_goal(self):
        pass

    def safety(self):
        print("You are in God's hands now my son.")

    def spin(self):
        r = rospy.Rate(2)
        cmd_msg = Twist()
        while not rospy.is_shutdown():
            cmd_msg.linear.x = 0.5
            self.pub.publish(cmd_msg)
            r.sleep()



