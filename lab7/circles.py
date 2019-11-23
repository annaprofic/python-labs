from lab6.points import Point
from math import sqrt, pi
import unittest


class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Radius can't be less than 0.")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):   # "Circle(x, y, radius)"
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return "%.4f" % (pi * self.radius ** 2)

    def move(self, x, y):
        self.pt = Point(self.pt.x + x, self.pt.y + y)
        return self

    def cover(self, other):
        covering_circle = self if self.radius > other.radius else other
        center_x = (self.pt.x + other.pt.x) // 2
        center_y = (self.pt.y + other.pt.y) // 2
        equation = round(sqrt(pow(covering_circle.pt.x - center_x, 2) + pow(covering_circle.pt.y - center_y, 2)), 2)

        covering_circle.pt = Point(center_x, center_y)
        covering_circle.radius += equation

        return covering_circle


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle1 = Circle(1, 2, 5)
        self.circle2 = Circle(-1, 2, 5)
        self.circle3 = Circle(0, 4, 7)
        self.circle4 = Circle(3, -2, 8)

    def test__repr__(self):
        self.assertEqual("Circle(1, 2, 5)", repr(self.circle1))
        self.assertEqual("Circle(-1, 2, 5)", repr(self.circle2))
        self.assertEqual("Circle(0, 4, 7)", repr(self.circle3))
        self.assertEqual("Circle(3, -2, 8)", repr(self.circle4))

    def test__eq__(self):
        self.assertTrue(self.circle1 == Circle(1, 2, 5))
        self.assertTrue(self.circle2 == Circle(-1, 2, 5))
        self.assertFalse(self.circle3 == Circle(1, 1, 1))
        self.assertFalse(self.circle4 == Circle(3, 2, 8))

    def test__ne__(self):
        self.assertFalse(self.circle1 != Circle(1, 2, 5))
        self.assertFalse(self.circle2 != Circle(-1, 2, 5))
        self.assertTrue(self.circle3 != Circle(1, 1, 1))
        self.assertTrue(self.circle4 != Circle(3, 2, 8))

    def test_area(self):
        self.assertEqual('78.5398', self.circle1.area())
        self.assertEqual('78.5398', self.circle2.area())
        self.assertEqual('153.9380', self.circle3.area())
        self.assertEqual('201.0619', self.circle4.area())

    def test_move(self):
        self.assertEqual(Circle(2, 4, self.circle1.radius), self.circle1.move(1, 2))
        self.assertEqual(self.circle2, self.circle2.move(0, 0))
        self.assertEqual(Circle(-1, -6, self.circle3.radius), self.circle3.move(-1, -10))
        self.assertEqual(Circle(1.5, 0.5, self.circle4.radius), self.circle4.move(-1.5, 2.5))

    def test_cover(self):
        self.assertEqual(Circle(0, 2, 6.0), self.circle1.cover(self.circle2))
        self.assertEqual(Circle(0, 3, 8.0), self.circle2.cover(self.circle3))
        self.assertEqual(Circle(1, 0, 10.83), self.circle3.cover(self.circle4))

    def tearDown(self):
        pass
