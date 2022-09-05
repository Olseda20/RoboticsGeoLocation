#!/usr/bin/python3

from shutil import move
import sys
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import rospy
import TurtleMotion
import PositionCalc


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
    distance_to_goal, theta_to_goal = PositionCalc.evaluate_distance(destination_location, pose)

    # compare current location to the goal location
    while distance_to_goal >= 1:
        distance_to_goal, theta_to_goal = PositionCalc.evaluate_distance(destination_location, pose)

        updated_linear_velocity = PositionCalc.calculate_linear_velocity(distance_to_goal, 0.5)
        updated_angular_velocity = PositionCalc.calculate_angular_velocity(theta_to_goal, pose.theta, 4)

        TurtleMotion.move_turtle(updated_linear_velocity, updated_angular_velocity, velocity_publisher, velocity)
        rospy.loginfo(distance_to_goal)
        rospy.loginfo(f'pose data: {pose.x} {pose.y}')
        # sleep(1)

    rospy.loginfo('goal has been reached')

if __name__ == "__main__":
    # create turtle node
    rospy.init_node('TurtleNode', anonymous=True)

    # velocity publisher
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # position subscriber
    position_subscriber = rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    time.sleep(2)

    rate = rospy.Rate(10)
    velocity = Twist()
    pose = Pose()

    move_to_goal([float(sys.argv[1]), float(sys.argv[2])], velocity_publisher)
    # while True:
    #     TurtleMotion.move_turtle(float(sys.argv[1]), float(sys.argv[2]), velocity_publisher, velocity)
    #     # pose = PositionCalc.get_current_pose(pose)
    #     rospy.loginfo(pose)