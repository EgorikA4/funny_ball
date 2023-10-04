"""Module for calculating the angle of rotation of the ball after a specified time."""

from math import pi


def degree(radius: float, time: float, acceleration: float, velocity: float = 0) -> float:
    """Calculate the angle of rotation of the ball.

    Args:
        radius: float - ball radius.
        time: float - moment in time.
        acceleration: float - ball acceleration.
        velocity: float - start ball speed.

    Returns:
        float - Rotation angle of the starting point.
    """
    full_degree = 360
    spatium = velocity * time + ((acceleration * time ** 2) / 2)
    length = 2 * pi * radius
    return round((spatium % length) / length * full_degree, 2)
