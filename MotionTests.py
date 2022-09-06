import pytest
import math
import motion

# preventing overly lengthy test lines
LIN_K = motion.LINEAR_VELOCITY_K
ANG_K = motion.ANGULAR_VELOCITY_K

def test_that_linear_velocity_is_correctly_evaluated():
  """ test to ensure that linear velocity is evaluated correctly """
  assert motion.calculate_linear_velocity(5, 5) == 25
  assert motion.calculate_linear_velocity(-5, 5) == -25
  assert motion.calculate_linear_velocity(12) == 12 * LIN_K
  assert motion.calculate_linear_velocity(12, 5) != 6

def test_that_angular_velocity_is_correctly_evaluated():
  """ test to ensure that angular velocity is evaluated correctly """
  assert motion.calculate_angular_velocity(10, 3, 5) == 35
  assert motion.calculate_angular_velocity(10, -3, 5) == 65
  assert motion.calculate_angular_velocity(10, 8) == (10 - 8) * ANG_K
  assert motion.calculate_angular_velocity(10, 8, 5) != 20
