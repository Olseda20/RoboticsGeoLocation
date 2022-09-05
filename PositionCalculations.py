#! /user/bin/python3

import sys
import math
import time
import rospy
from turtlesim.msg import Pose

def pose_callback(pose_message):
    ''' callback function to globally store the currently pose data '''
    global pose, X, Y, YAW
    pose = pose_message
    X = pose.x
    Y = pose.y
    YAW = pose.theta

def initiate_velocity_publisher():
    ''' initations pose subscriber '''
    rospy.init_node('TurtleMotion', anonymous=True)
    position_subscriber = rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    time.sleep(2)

def callback(pose):
    rospy.loginfo(f'Location x: {pose.x} \t Location y: {pose.y}')

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


# def move_to_goal(self, goal_location=DesiredLocation):
#     # desired location of robotics

#     # update turtle position and evlauate distance
    # # self.update_pose()
    # x_dist = self.pose.x - goal_location[1]
    # y_dist = self.pose.y - goal_location[2]

    

    # motion controller
        # enter TurtleModtion.py to evaluate how fast the turtleshould move?
        # PID?

# currently this file will work on the turlsim map thing

# but the idea is that once we can import a gps location, that will act as the coordiante positions of the turtle and the 
# coordinate location of Greenwhich will be the desired location. 

# setting a temporary coordiante location

# def TurtlePosition():
#     rospy.init_node('TurtleLocation', anonymous=True)
#     subscriber = rospy.Subscriber('/turtle1/pose', Twist, queue_size=10)
#     rate = rospy.Rate(10)

#     pose = subscriber.pose

#     while True:
#         rospy.loginfo(pose)


if __name__ == "__main__":
    print('hello world')
    # turt = TurtleLocation()

    while True:
        rospy.loginfo(turt.callback(turt.odometry))