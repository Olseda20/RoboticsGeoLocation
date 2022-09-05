import pytest
import math
import TurtleMotion

def test_that_linear_velocity_is_correctly_evaluated():
  ''' test to ensure that linear velocity is evaluated correctly '''

  assert TurtleMotion.calculate_linear_velocity(5, 5) == 25
  assert TurtleMotion.calculate_linear_velocity(12) == 6
  assert TurtleMotion.calculate_linear_velocity(12, 5) != 6

def test_that_angular_velocity_is_correctly_evaluated():
  ''' test to ensure that angular velocity is evaluated correctly '''

  assert TurtleMotion.calculate_angular_velocity(10, 3, 5) == 35
  assert TurtleMotion.calculate_angular_velocity(10, 8) == 20
  assert TurtleMotion.calculate_angular_velocity(10, 8, 5) != 20
