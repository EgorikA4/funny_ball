# review for:
# Kolkareva
# Kuznetsova
def degree(radius: float,
           time: float,
           acceleration: float,
           velocity: float = 0) -> float:
    spatium = velocity*time+((acceleration*time**2)/2)