from numpy.random import rand

from geometry_msgs.msg import Twist, Point
from std_srvs.srv import Trigger
from std_srvs.srv import TriggerResponse

import rospy

class Robot:
        """Robot class for controlling its behavior.

	Attributes:
        frequency (int): frequency rate for sending commands to the robot.
        is_moving (bool): flag to start and stop the robot, initially False.
        cmd_pub (:obj:Publisher): publisher for command velocities.

        """	
   def __init__(self, frequency=1):

        """Constructor.
        Args:
            frequency (int, optional): frequency frequency rate for sending commands to the robot.
        """
      self.frequency = frequency
      self.is_moving = True
      self.cmd_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
      self.header_sub = rospy.Subscriber("heading_point", Point, header_callback)
#        self.start_stop_srv = rospy.Service("start_stop", Trigger, self.handle_start_stop_robot)

"""    def handle_start_stop_robot(self, req):
        self.is_moving = not self.is_moving
        return TriggerResponse(True, "Robot moving: {}".format(self.is_moving))
"""
   def header_callback(h_point):
      print("Point is:"h_point.x, h_point.y, h_point.z) 

   def spin(self):
      r = rospy.Rate(2)
      while not rospy.is_shutdown():
         if self.is_moving:
         linear_vel_x = 1
              # rospy.logdebug("{} {}".format(linear_vel_x, angular_vel_z))
         cmd_msg = Twist()
         cmd_msg.linear.x = linear_vel_x
              # cmd_msg.angular.z = angular_vel_z
         self.cmd_pub.publish(cmd_msg)
      r.sleep() 
             

