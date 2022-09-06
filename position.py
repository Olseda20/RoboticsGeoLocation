#! /user/bin/python3

## File containng helper methods identifying the positional evaluations of the turtle

import math

def evaluate_distance(goal_location, current_pose):
  """ evaluates the distance from the turtle location to the goal location """
  distance_to_goal_x = goal_location[0] - current_pose.x
  distance_to_goal_y = goal_location[1] - current_pose.y

  distance_to_goal = math.sqrt(distance_to_goal_x**2 + distance_to_goal_y**2)
  theta_to_goal = math.atan2(distance_to_goal_y, distance_to_goal_x)

  return distance_to_goal, theta_to_goal