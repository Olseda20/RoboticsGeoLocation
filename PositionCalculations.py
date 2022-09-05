#! /user/bin/python3

import sys
import math
import time
import rospy
from turtlesim.msg import Pose

POSE = None

def initiate_velocity_publisher():
    ''' initations pose subscriber '''

    def callback(pose_message):
        global POSE
        POSE = pose_message

    rospy.init_node('TurtleMotion', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    time.sleep(2)


def get_current_pose(pose):
    """ Callback function which is called when a new message of type Pose is received 
    by the subscriber. """
    # pose = data
    pose.x = round(pose.x, 4)
    pose.y = round(pose.y, 4)

def evaluate_distance(goal_location, current_pose):
    ''' evaludates the distance from the turtle location to the goal location '''
    distance_to_goal_x = goal_location[0] - current_pose.x
    distance_to_goal_y = goal_location[1] - current_pose.y

    distance_to_goal = math.sqrt(distance_to_goal_x**2 + distance_to_goal_y**2)
    theta_to_goal = math.atan2(distance_to_goal_y, distance_to_goal_x)

    return distance_to_goal, theta_to_goal

def calculate_linear_velocity(distance_to_goal, k = 0.8):
    ''' calculates the desired linear velovity with proprtional control (k) '''
    linear_velocity = distance_to_goal*k
    return linear_velocity

def calculate_angular_velocity(theta_goal, theta, k = 9):
    ''' calculates the desired angular velovity with proprtional control (k) '''
    angular_velocity = (theta_goal - theta)*k
    return angular_velocity

def main():
    ''' main run method '''
    print('TODO')

if __name__ == "__main__":
    main()
