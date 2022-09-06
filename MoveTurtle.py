#!/usr/bin/python3

import sys
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import rospy
import motion
import position

WINDOW_BOUNDARY = [11.0, 11.0]

class Turtle():
  ''' Class to contain an instance of a turtle for motion around a space '''
  def __init__(self) -> None:
    # initlise pose and velocity
    self.pose = Pose()
    self.velocity = Twist()
    self.linear_k = 1
    self.angular_k = 10

    # create turtle node
    rospy.init_node('TurtleNode', anonymous=True)

    # velocity publisher
    self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # position subscriber
    rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
    time.sleep(2)
    self.rate = rospy.Rate(10)

  def pose_callback(self, pose_message):
    ''' callback function to globally store the currently pose data '''
    self.pose = pose_message

  def move_turtle(self, linear_vel, angular_vel):
    ''' publishes linear and angular velocities to the turtle '''
    # setting linear velocities
    self.velocity.linear.x = linear_vel
    self.velocity.linear.y = 0
    self.velocity.linear.z = 0
    # setting angular velocities
    self.velocity.angular.x = 0
    self. velocity.angular.y = 0
    self.velocity.angular.z = angular_vel

    # for logging/debugging
    # rospy.loginfo(f'\nLinear Velocity: {linear_vel} \t Angular Velocity: {angular_vel}')
    self.velocity_publisher.publish(self.velocity)

  def move_to_goal(self, destination_location):
    ''' method to move turtle to desired goal location '''

    try:
      # identify/initialise the distance and theta to goal
      distance_to_goal, theta_to_goal = position.evaluate_distance(destination_location, self.pose)

      # compare current location to the goal location
      while distance_to_goal >= 1:
        distance_to_goal, theta_to_goal = position.evaluate_distance(destination_location, self.pose)

        updated_linear_velocity = motion.calculate_linear_velocity(distance_to_goal, self.linear_k)
        updated_angular_velocity = motion.calculate_angular_velocity(theta_to_goal, self.pose.theta, self.angular_k)

        self.move_turtle(updated_linear_velocity, updated_angular_velocity)
        rospy.loginfo(f'distance to goal: {distance_to_goal}')
        rospy.loginfo(f'pose data: {self.pose.x} {self.pose.y}')
        self.rate.sleep()

      rospy.loginfo('goal has been reached')
    except rospy.ROSInterruptException:
      pass

def main(goal_x = None, goal_y = None):
  ''' main run script - to move turtle to a specified goal location '''

  if (goal_x is None) or (goal_y is None):
    print("the goal location cannot be None")
    return 0

  if ((goal_x < 0) or (goal_x > 11)) or ((goal_y < 0) or (goal_y > 11)):
    print("Goal coordiante for x and y must be between 0 and 11")
    return 0

  turtle = Turtle()
  turtle.move_to_goal([goal_x, goal_y])

if __name__ == "__main__":
  try:
    if (float(sys.argv[1]) <= WINDOW_BOUNDARY[0]) or (float(sys.argv[2]) <= WINDOW_BOUNDARY[1]):
      main(float(sys.argv[1]), float(sys.argv[2]))
    else: 
      print("Please provide some coordinates, eg 'run.py 3 4'")

  except rospy.ROSInterruptException:
    pass
