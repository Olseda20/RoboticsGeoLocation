#!/usr/bin/python3

import sys
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import rospy
import TurtleMotion
import PositionCalculations as PoseCalc


def pose_callback(pose_message):
    ''' callback function to globally store the currently pose data '''
    global pose, X, Y, YAW
    pose = pose_message
    X = pose.x
    Y = pose.y
    YAW = pose.theta

def move_to_goal(destination_location, velocity_publisher):
    ''' method to move turtle to desired goal location '''
    # identify goal location
    # initialise distance and theta to goal
    distance_to_goal, theta_to_goal = PoseCalc.evaluate_distance(destination_location, pose)

    # compare current location to the goal location
    while distance_to_goal >= 1:
        distance_to_goal, theta_to_goal = PoseCalc.evaluate_distance(destination_location, pose)

        updated_linear_velocity = PoseCalc.calculate_linear_velocity(distance_to_goal, 0.5)
        updated_angular_velocity = PoseCalc.calculate_angular_velocity(theta_to_goal, pose.theta, 4)

        TurtleMotion.move_turtle(updated_linear_velocity, updated_angular_velocity, velocity_publisher, velocity)
        rospy.loginfo(distance_to_goal)
        rospy.loginfo(f'pose data: {pose.x} {pose.y}')
        # sleep(1)

    rospy.loginfo('goal has been reached')

def main(goal_x = None, goal_y = None):
    ''' main run script - to move turtle to a specified goal location '''
    
    if ((goal_x is None) or (goal_y is None)):
        rospy.loginfo("Please prove a goal location in the to the method")
        return 0
    # create turtle node
    rospy.init_node('TurtleNode', anonymous=True)

    # velocity publisher
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # position subscriber
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    time.sleep(2)

    rate = rospy.Rate(10)
    velocity = Twist()
    pose = Pose()

    move_to_goal([goal_x, goal_y], velocity_publisher)

if __name__ == "__main__":
    main(float(sys.argv[1]), float(sys.argv[2]))

    # while True:
    #     TurtleMotion.move_turtle(float(sys.argv[1]), float(sys.argv[2]), velocity_publisher, velocity)
    #     # pose = PoseCalc.get_current_pose(pose)
    #     rospy.loginfo(pose)