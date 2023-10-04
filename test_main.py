"""Angle calculation testing module."""
from typing import Tuple

import pytest

from calculate_degree import degree

positive_tests_with_velocity = [
    ((17.39, 50.39, 6.71, 18.63), 200.54),
    ((6.03, 36.64, 21.94, 27.86), 233.21),
    ((2.32, 52.53, 14.82, 33.55), 217.0),
    ((4.19, 14.12, 4.32, 20.03), 36.31),
    ((16.89, 25.12, 9.22, 28.7), 73.74),
    ((2.13, 6.87, 7.9, 16.98), 232.69),
    ((5.91, 43.68, 11.5, 24.18), 316.92),
    ((19.45, 37.15, 24.48, 9.43), 34.47),
    ((8.2, 25.08, 16.44, 12.73), 198.13),
    ((5.01, 27.58, 16.65, 25.97), 331.13),
    ((16.71, 26.23, 8.93, 22.96), 358.28),
    ((11.44, 11.88, 11.08, 5.95), 309.99),
    ((8.1, 40.91, 4.89, 26.02), 114.77),
    ((9.81, 32.99, 15.83, 1.84), 266.25),
    ((8.27, 46.47, 11.29, 3.24), 178.33),
    ((17.27, 4.98, 23.68, 19.11), 209.92),
    ((2.7, 33.91, 11.07, 4.75), 239.72),
    ((9.28, 17.46, 3.15, 33.66), 113.0),
    ((9.66, 35.71, 3.43, 22.74), 147.91),
    ((4.7, 52.47, 15.59, 29.07), 129.57),
]

positive_tests_without_velocity = [
    ((19.04, 50.72, 7.38), 125.42),
    ((16.31, 59.31, 12.74), 236.17),
    ((19.23, 41.07, 4.59), 13.88),
    ((9.53, 39.41, 18.73), 328.1),
    ((6.33, 20.81, 20.99), 98.22),
    ((19.82, 36.3, 1.81), 207.31),
    ((11.32, 26.65, 10.37), 278.86),
    ((14.95, 23.64, 17.36), 230.72),
    ((19.36, 37.03, 9.82), 125.36),
    ((14.19, 43.64, 10.56), 281.65),
    ((18.82, 18.65, 11.32), 233.45),
    ((5.67, 43.8, 4.22), 224.42),
    ((5.04, 6.14, 13.89), 96.47),
    ((1.33, 37.83, 2.15), 35.37),
    ((19.67, 26.99, 11.77), 247.36),
    ((7.25, 32.07, 9.36), 238.94),
    ((2.26, 7.09, 15.49), 150.25),
    ((4.95, 12.16, 23.11), 336.73),
    ((17.16, 58.52, 18.57), 328.55),
    ((8.63, 42.38, 19.12), 236.53),
]


@pytest.mark.parametrize('args, expected', positive_tests_with_velocity)
def test_positive_calculate_with_velocity(args: Tuple[float], expected: float):
    """Positive test calculate degree with velocity.

    Args:
        args: Tuple[float] - parameters for calculation
        expected: float - angle of rotation
    """
    assert degree(*args) == expected


@pytest.mark.parametrize('args, expected', positive_tests_without_velocity)
def test_positive_calculate_without_velocity(args: Tuple[float], expected: float):
    """Positive test calculate degree without velocity.

    Args:
        args: Tuple[float] - all parameters except velocity
        expected: float - angle of rotation
    """
    assert degree(*args) == expected


negative_tests_division_by_zero = [
    (0, 8.78, 47.86, 39.45),
    (0, 4.04, 77.55, 36.99),
    (0, 10.62, 67.23, 27.02),
    (0, 26.44, 13.25, 43.93),
    (0, 20.33, 82.18, 4.9),
    (0, 49.12, 33.52, 19.78),
    (0, 27.12, 13.9, 18.55),
    (0, 56.58, 43.85, 9.82),
    (0, 10.74, 23.48, 8.36),
    (0, 46.15, 95.82, 8.38),
]


@pytest.mark.xfail(negative_tests_division_by_zero, reason=ZeroDivisionError)
def test_negative_calculate_by_zero(args):
    """Negative test calculate with radius equal zero.

    Args:
        args: Tuple[float] - all parameters
    """
    assert degree(*args)


tests_with_negative_values = [
    (-18.27, -2.72, -49.14, -3.17),
    (-9.96, -48.69, -87.27, -40.84),
    (-8.55, -54.88, -9.04, -43.45),
    (-12.59, -38.01, -48.75, -17.73),
    (-5.16, -4.8, -43.78, -21.72),
    (-14.51, -0.53, -80.14, -26.04),
    (-20.8, -48.16, -56.48, -19.54),
    (-7.82, -56.72, -80.14, -22.69),
    (-3.13, -48.06, -78.28, -12.74),
    (-13.38, -57.18, -54.01, -31.63),
]


@pytest.mark.xfail(tests_with_negative_values, reason=Exception)
def test_calcuate_with_negative_params(args):
    """Test calculate with negative parametrs.

    Args:
        args: Tuple[float] - negative parameters
    """
    assert degree(*args)
