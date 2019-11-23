from lab6.points import Point
import math

class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Radius can't be less than 0.")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):   # "Circle(x, y, radius)"
        return f"Circle({self.x}, {self.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * self.radius ** 2

    def move(self, x, y):
        self.x += x
        self.y += y

    def cover(self, other): pass  # okrąg pokrywający oba


# Kod testujący moduł.

import unittest


class TestCircle(unittest.TestCase): pass
