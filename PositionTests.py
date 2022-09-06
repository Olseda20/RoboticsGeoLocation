import pytest
import math
from turtlesim.msg import Pose
import position as PoseCalc

pose = Pose()
pose.x = pose.y = 0

def test_that_evaluate_distance_evaluates_correctly_when_moving_north_and_east():
  """ check if evaluate_distance method is correct when the goal in in the north east """
  goal = [3,4]
  assert PoseCalc.evaluate_distance(goal, pose) == (5, math.atan(4/3))

def test_that_evaluate_distance_evaluates_correctly_when_moving_south_and_east():
  """ check if evaluate_distance method is correct when the goal in in the south east """
  goal = [3,-4]
  assert PoseCalc.evaluate_distance(goal, pose) == (5, -math.atan(4/3))

def test_that_evaluate_distance_evaluates_correctly_when_moving_north_and_west():
  """ check if evaluate_distance method is correct when the goal in in the north west """
  goal = [-3,4]
  assert PoseCalc.evaluate_distance(goal, pose) == (5, math.pi - math.atan(4/3))

def test_that_evaluate_distance_evaluates_correctly_when_moving_south_and_west():
  """ check if evaluate_distance method is correct when the goal in in the south west """
  goal = [-3,-4]
  assert PoseCalc.evaluate_distance(goal, pose) == (5, -(math.pi - math.atan(4/3)))
