import pytest
import math

import PositionCalculations as PoseCalc
import TurtleMotion

def test_that_evaluate_distance_evaluates_correctly():
  ''' test to ensure that the linear and angular distances are correctly evaluated b'''
  assert PoseCalc.evaluate_distance((0, 0), (3, 4)) == 5, math.atan(3/4)
  assert PoseCalc.evaluate_distance((0, 0), (3, -4)) == 5, math.pi - math.atan(3/4)
  assert PoseCalc.evaluate_distance((0, 0), (-3, 4)) == 5, -math.atan(3/4)
  assert PoseCalc.evaluate_distance((0, 0), (-3, -4)) == 5, -(math.pi-math.atan(3/4))


def test_that_linear_velocity_is_correctly_evaluated():
  ''' test to ensure that linear velocity is evaluated correctly '''
  PoseCalc.calculate_linear_velocity

def test_that_angular_velocity_is_correctly_evaluated():
  ''' test to ensure that angular velocity is evaluated correctly '''
  PoseCalc.calculate_angular_velocity