from lab6.points import Point
import math
import unittest

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
        return "%.4f" % (math.pi * self.radius ** 2)

    def move(self, x, y):
        self.pt += Point(x, y)
        return self

    def cover(self, other): pass  # okrąg pokrywający oba


# Kod testujący moduł.


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle1 = Circle(1, 2, 5)
        self.circle2 = Circle(-1, 2, 5)
        self.circle3 = Circle(0, 4, 7)
        self.circle4 = Circle(3, -2, 8)

    def test_area(self):
        self.assertEqual('78.5398', self.circle1.area())
        self.assertEqual('78.5398', self.circle2.area())
        self.assertEqual('153.9380', self.circle3.area())
        self.assertEqual('201.0619', self.circle4.area())

    def test_move(self):
        self.assertEqual(self.circle1, self.circle1.move(1, 2))
        self.assertEqual('', self.circle1.move(0, 0))
        self.assertEqual('', self.circle1.move(-1, -10))
        self.assertEqual('', self.circle1.move(-1.5, 2.5))

    def tearDown(self):
        pass
