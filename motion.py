#!/usr/bin/python3

## File containng helper methods for the motion of the turtle

# Default values for the proportional contants
LINEAR_VELOCITY_K = 0.8
ANGULAR_VELOCITY_K = 10

def calculate_linear_velocity(distance_to_goal, k = LINEAR_VELOCITY_K):
  """ calculates the desired linear velocity with proprtional control (k) """
  linear_velocity = distance_to_goal*k
  return linear_velocity

def calculate_angular_velocity(theta_goal, theta, k = ANGULAR_VELOCITY_K):
  """ calculates the desired angular velocity with proprtional control (k) """
  angular_velocity = (theta_goal - theta)*k
  return angular_velocity
