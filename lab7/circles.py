from lab6.points import Point
from math import sqrt, pi
import unittest


class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Radius can't be less than 0.")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Second argument must be a Circle.")

        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return "%.4f" % (pi * self.radius ** 2)

    def move(self, x, y):
        self.pt = Point(self.pt.x + x, self.pt.y + y)
        return self

    def cover(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Second argument must be a Circle.")

        covering_circle = self if self.radius > other.radius else other
        center_x = (self.pt.x + other.pt.x) // 2
        center_y = (self.pt.y + other.pt.y) // 2
        equation = round(sqrt(pow(covering_circle.pt.x - center_x, 2) + pow(covering_circle.pt.y - center_y, 2)), 2)

        covering_circle.pt = Point(center_x, center_y)
        covering_circle.radius += equation

        return covering_circle
