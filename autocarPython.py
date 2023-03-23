#!/usr/bin/env python3
from ctypes import _NamedFuncPointer
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time
import readchar  # install using pip: pip install readchar

def scan_callback(scan_msg):
    # detect obstacles within a certain range
    if min(scan_msg.ranges) < 0.5:
        # stop the robot if an obstacle is detected
        vel_msg.linear.x = 0
        vel_pub.publish(vel_msg)
    else:
        # move the robot based on keyboard input
        key = readchar.readkey()
        if key == 'w':
            vel_msg.linear.x = 0.5
            vel_msg.angular.z = 0
        elif key == 'a':
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0.5
        elif key == 's':
            vel_msg.linear.x = -0.5
            vel_msg.angular.z = 0
        elif key == 'd':
            vel_msg.linear.x = 0
            vel_msg.angular.z = -0.5
        else:
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
        vel_pub.publish(vel_msg)

if __name__ == '_main_':
    rospy.init_node('simple_robot')
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    scan_sub = rospy.Subscriber('/scan', LaserScan, scan_callback)
    vel_msg = Twist()

    while not rospy.is_shutdown():
        # wait for new laser scan messages
        time.sleep(0.01)


        