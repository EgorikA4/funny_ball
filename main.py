"""Module for calculating the angle of rotation of the ball after a specified time."""
# review for:
# Kolkareva
# Kuznetsova


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
    spatium = velocity * time + ((acceleration * time ** 2) / 2)
    length = 2 * 3.14 * radius
    return (spatium % length) / length * 360
