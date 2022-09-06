#!/usr/bin/python3

import sys
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import rospy
import TurtleMotion
import PositionCalculations as PoseCalc

POSE = Pose()
velocity = Twist()

def pose_callback(pose_message):
  ''' callback function to globally store the currently pose data '''
  global POSE
  POSE = pose_message

def move_to_goal(destination_location, velocity_publisher):
  ''' method to move turtle to desired goal location '''
  # identify goal location
  # initialise distance and theta to goal
  distance_to_goal, theta_to_goal = PoseCalc.evaluate_distance(destination_location, POSE)

  # compare current location to the goal location
  while distance_to_goal >= 0.1:
    distance_to_goal, theta_to_goal = PoseCalc.evaluate_distance(destination_location, POSE)

    updated_linear_velocity = TurtleMotion.calculate_linear_velocity(distance_to_goal, 0.5)
    updated_angular_velocity = TurtleMotion.calculate_angular_velocity(theta_to_goal, POSE.theta, 4)

    TurtleMotion.move_turtle(updated_linear_velocity, updated_angular_velocity, velocity_publisher, velocity)
    rospy.loginfo(f'distance to goal: {distance_to_goal}')
    rospy.loginfo(f'pose data: {POSE.x} {POSE.y}')

  rospy.loginfo('goal has been reached')

def main(goal_x = None, goal_y = None):
  ''' main run script - to move turtle to a specified goal location '''
  
  if (goal_x is None) or (goal_y is None):
    rospy.loginfo("the goal location cannot be None")
    return 0

  if ((goal_x >= 11) or (goal_y >= 11)):
    rospy.loginfo("Goal coordiante for x and y must be between 0 and 11")
    return 0

  # create turtle node
  rospy.init_node('TurtleNode', anonymous=True)

  # velocity publisher
  velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

  # position subscriber
  rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
  time.sleep(2)
  rospy.Rate(10)

  move_to_goal([goal_x, goal_y], velocity_publisher)

if __name__ == "__main__":
  try:
    #
    main(float(sys.argv[1]), float(sys.argv[2]))
    #else: 
     # print("Please provide some coordinates, eg 'run.py 3 4'")

  except rospy.ROSInterruptException:
    pass
  # while True:
  #     TurtleMotion.move_turtle(float(sys.argv[1]), float(sys.argv[2]), velocity_publisher, velocity)
  #     # pose = PoseCalc.get_current_pose(pose)
  #     rospy.loginfo(pose)
