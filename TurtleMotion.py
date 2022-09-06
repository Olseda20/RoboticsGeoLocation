#!/usr/bin/python3

import sys
import math
import rospy
from geometry_msgs.msg import Twist

def initiate_velocity_publisher():
  ''' initations velcity publisher '''
  rospy.init_node('TurtleMotion', anonymous=True)
  return rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

def calculate_linear_velocity(distance_to_goal, k = 0.8):
  ''' calculates the desired linear velocity with proprtional control (k) '''
  linear_velocity = distance_to_goal*k
  return linear_velocity

def calculate_angular_velocity(theta_goal, theta, k = 10):
  ''' calculates the desired angular velocity with proprtional control (k) '''
  angular_velocity = (theta_goal - theta)*k
  return angular_velocity

def move_turtle(linear_vel, angular_vel, pub , velocity):
  ''' publishes linear and angular velocities to the turtle '''
  # setting linear velocities
  velocity.linear.x = linear_vel
  velocity.linear.y = 0
  velocity.linear.z = 0
  # setting angular velocities
  velocity.angular.x = 0
  velocity.angular.y = 0
  velocity.angular.z = angular_vel

  # for logging/debugging
  # rospy.loginfo(f'\nLinear Velocity: {linear_vel} \t Angular Velocity: {angular_vel}')
  pub.publish(velocity)

if __name__ == "__main__":
  try:
    publisher = initiate_velocity_publisher()
    rate = rospy.Rate(10)
    vel = Twist()
    while True:
      move_turtle(float(sys.argv[1]), float(sys.argv[2]), publisher, vel)

  except rospy.ROSInterruptException:
    pass