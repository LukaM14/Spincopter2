#!/usr/bin/env python

__author__ = 'LukaM'

import rospy
import math
import numpy
from mav_msgs.msg import Actuators
from std_msgs.msg import Float64

class VelocityPublisher:

    def __init__(self):
 
        #self.pub_motor = rospy.Publisher('/spincopter/gazebo/command/motor_speed', Actuators, queue_size=1)
        rospy.sleep(0.1)
        self.ros_rate = rospy.Rate(10)

    def run(self):

        while not rospy.is_shutdown():
            self.ros_rate.sleep()
            newMsg = Actuators()
            #newMsg.angular_velocities = Float64()
            speed1 = 800
            speed2 = 800
            #print "Starting publishing newMsg"

            #newMsg.angular_velocities = [speed1, speed2] 
            #self.pub_motor.publish(newMsg)
            #rospy.spin()


if __name__ == '__main__':

    rospy.init_node('mav_vel_publisher')
    vel_pub = VelocityPublisher()
    print "Starting publishing"
    vel_pub.run()
