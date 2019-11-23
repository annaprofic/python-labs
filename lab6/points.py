import math
import unittest


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class TestPoint(unittest.TestCase):

    def test_print(self):
        self.assertEqual("Point(6, 1)", repr(Point(6, 1)))
        self.assertEqual("Point(11, 3)", repr(Point(11, 3)))
        self.assertEqual("Point(2, 2)", repr(Point(2, 2)))
        self.assertEqual("Point(12, -2)", repr(Point(12, -2)))
        self.assertEqual("(6, 6)", str(Point(6, 6)))
        self.assertEqual("(11, 3)", str(Point(11, 3)))
        self.assertEqual("(0, 2)", str(Point(0, 2)))
        self.assertEqual("(2, -2)", str(Point(2, -2)))

    def test_cmp(self):
        self.assertTrue(Point(1, 0) == Point(1, 0))
        self.assertTrue(Point(1, 3) != Point(2, 9))
        self.assertTrue(Point(3, 10) == Point(3, 10))
        self.assertTrue(Point(1, 11) != Point(1, 9))
        self.assertTrue(Point(9, 8) == Point(9, 8))
        self.assertTrue(Point(8, 77) != Point(0, 0))

    def test_add(self):
        self.assertEqual(Point(1, 0), Point(0, -1) + Point(1, 1))
        self.assertEqual(Point(1, 3), Point(1, -5) + Point(0, 8))
        self.assertEqual(Point(3, 10), Point(2, 5) + Point(1, 5))
        self.assertEqual(Point(1, 11), Point(-30, 1) + Point(31, 10))
        self.assertEqual(Point(9, 8), Point(10, 9) + Point(-1, -1))
        self.assertEqual(Point(8, 77), Point(8, 0) + Point(0, 77))

    def test_sub(self):
        self.assertEqual(Point(-1, -2), Point(0, -1) - Point(1, 1))
        self.assertEqual(Point(1, -13), Point(1, -5) - Point(0, 8))
        self.assertEqual(Point(1, 0), Point(2, 5) - Point(1, 5))
        self.assertEqual(Point(-61, -9), Point(-30, 1) - Point(31, 10))
        self.assertEqual(Point(11, 10), Point(10, 9) - Point(-1, -1))
        self.assertEqual(Point(8, -77), Point(8, 0) - Point(0, 77))

    def test_mul(self):
        self.assertEqual(-1, Point(0, -1) * Point(1, 1))
        self.assertEqual(-40, Point(1, -5) * Point(0, 8))
        self.assertEqual(27, Point(2, 5) * Point(1, 5))
        self.assertEqual(1, Point(-3, 1) * Point(3, 10))
        self.assertEqual(-19, Point(10, 9) * Point(-1, -1))
        self.assertEqual(0, Point(8, 0) * Point(0, 1))

    def test_cross(self):
        self.assertEqual(1, Point(0, -1).cross(Point(1, 1)))
        self.assertEqual(-2, Point(2, 4).cross(Point(2, 3)))
        self.assertEqual(16, Point(10, 2).cross(Point(2, 2)))
        self.assertEqual(0, Point(-1, -1).cross(Point(1, 1)))
        self.assertEqual(0, Point(-6, 4).cross(Point(6, -4)))
        self.assertEqual(-300, Point(10, 20).cross(Point(20, 10)))

    def test_length(self):
        self.assertEqual(1, Point(0, -1).length())
        self.assertEqual(5, Point(3, 4).length())
        self.assertEqual(10, Point(6, 8).length())


if __name__ == "__main__":
    unittest.main()
