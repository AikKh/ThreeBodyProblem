from math import sqrt


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.X: float = x
        self.Y: float = y

    @property
    def length(self) -> float:
        return sqrt(self.X ** 2 + self.Y ** 2)
    
    def normalize(self):
        "Returns new normalized vector"
        l = self.length
        return Vector(self.X / l, self.Y / l)

    def __add__(self, other):
        if type(other) is float:
            return Vector(self.X + other, self.Y + other)
        return Vector(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other):
        if type(other) is float:
            return Vector(self.X - other, self.Y - other)
        return Vector(self.X - other.X, self.Y - other.Y)

    def __mul__(self, other: float):
        return Vector(self.X * other, self.Y * other)

    def __truediv__(self, other: float):
        return Vector(self.X / other, self.Y / other)
    
    def __iter__(self):
        yield self.X
        yield self.Y

    def __str__(self):
        return f"X: {self.X}, Y: {self.Y}"