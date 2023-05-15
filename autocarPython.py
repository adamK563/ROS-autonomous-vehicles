#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# Function to get keyboard inputs
def getch():
    # Save the terminal attributes
    old_attr = termios.tcgetattr(sys.stdin)
    try:
        # Set the terminal attributes for reading input
        tty.setraw(sys.stdin.fileno())
        # Read a single character from the user
        ch = sys.stdin.read(1)
    finally:
        # Restore the terminal attributes
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
    return ch

def move():
    # Initialize the ROS node
    rospy.init_node('turtlebot3_controller')

    # Create a publisher object to control the robot's velocity
    velocity_publisher = rospy.Publisher('/turtlebot3/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Set the default linear and angular velocities
    linear_speed = 0.2
    angular_speed = 0.5

    # Display the instructions
    print("Control TurtleBot3 in Gazebo Simulation")
    print("Use the following keys:")
    print("  W : Move Forward")
    print("  S : Move Backward")
    print("  A : Turn Left")
    print("  D : Turn Right")
    print("  X : Stop")
    print("  Q : Quit")

    while True:
        # Get the user input
        key = getch()

        # Move Forward
        if key == 'W':
            vel_msg.linear.x = linear_speed
            vel_msg.angular.z = 0.0

        # Move Backward
        elif key == 'S':
            vel_msg.linear.x = -linear_speed
            vel_msg.angular.z = 0.0

        # Turn Left
        elif key == 'A':
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = angular_speed

        # Turn Right
        elif key == 'D':
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = -angular_speed

        # Stop
        elif key == 'X':
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.0

        # Quit
        elif key == 'Q':
            break

        # Publish the velocity commands
        velocity_publisher.publish(vel_msg)

    # Stop the robot before exiting
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
