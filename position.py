from math import hypot


class Position:
    x: float
    y: float

    def __init__(self, line: str):
        self.x, self.y = map(float, line.split())

    def distance_from(self, pos):
        return hypot(self.x - pos.x, pos.x, self.y - pos.y)