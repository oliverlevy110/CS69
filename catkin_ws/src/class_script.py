import rospy
from geometry_msgs.msg import Twist

def spin():
    r = rospy.Rate(1)
    i=0
    while not rospy.is_shutdown():
        i += 1
        if (i%2 == 0):
            cmd_msg = Twist()
            cmd_msg.linear.x = 0.5
            for i in range(0,6):
                pub[i].publish(cmd_msg)
        else: 
            cmd_msg = Twist()
            cmd_msg.linear.x = -0.5
            for i in range(0,6):
                pub[i].publish(cmd_msg)
if __name__ == "__main__":
    rospy.init_node("counter_vel_node")
    pub=[]
    for i in range(0,6):    
        pub.append(rospy.Publisher("/robot_"+str(i)+"/cmd_vel",Twist, queue_size=1))
    spin()
