# review for:
# Kolkareva
# Kuznetsova
PI = 3.14


def degree(radius: float,
           time: float,
           acceleration: float,
           velocity: float = 0) -> float:
    spatium = velocity * time + ((acceleration * time ** 2) / 2)
    length = 2 * PI * radius
    return (spatium % length) / length * 360
