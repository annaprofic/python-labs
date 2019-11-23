import unittest
import math
import numpy as np


class Frac:
    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Denominator cannot be equal to zero")
        self.x = x
        self.y = y
        self.lowest_frac()

    def __str__(self):
        if self.y == 1:
            return f"{self.x}"
        return f"{self.x}/{self.y}"

    def __repr__(self):
        return f"Frac({self.x}, {self.y})"

    def lowest_frac(self):
        common_factor = math.gcd(self.x, self.y)
        self.x = int(self.x / common_factor)
        self.y = int(self.y / common_factor)

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y
    #
    # def __ne__(self, other):
    #     return not self == other
    #
    # def __lt__(self, other):
    #     return self.x < other
    #
    # def __le__(self, other):
    #     pass

    # def __gt__(self, other): pass

    # def __ge__(self, other): pass

    def __add__(self, other):  # frac1+frac2, frac+int
        if not isinstance(other, (Frac, int)):
            raise ValueError("Invalid value format, it must be Frac or Integer value.")

        if isinstance(other, Frac):
            if self.y == other.y:
                self.x += other.x
                return self.lowest_frac()
            lcm = np.lcm(self.y, other.y)
            return Frac(self.x * (lcm // self.y) + other.x * (lcm // other.y), lcm)

        if isinstance(other, int):
            return Frac(self.x + self.y * other, self.y)

    def __sub__(self, other):  # frac1-frac2, frac-int
        if not isinstance(other, (Frac, int)):
            raise ValueError("Invalid value format, it must be Frac or Integer value.")

        if isinstance(other, Frac):
            if self.y == other.y:
                self.x -= other.x
                return self.lowest_frac()
            lcm = np.lcm(self.y, other.y)
            return Frac(self.x * (lcm // self.y) - other.x * (lcm // other.y), lcm)

        if isinstance(other, int):
            return Frac(self.x - self.y * other, self.y)

    def __rsub__(self, other):
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        if not isinstance(other, (Frac, int)):
            raise ValueError("Invalid value format, it must be Frac or Integer value.")

        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)

        if isinstance(other, int):
            return Frac(self.x * other, self.y)

    def __div__(self, other):  # frac1/frac2, frac/int
        if not isinstance(other, (Frac, int)):
            raise ValueError("Invalid value format, it must be Frac or Integer value.")

        if isinstance(other, Frac):
            return self * Frac(other.y, other.x)

        if isinstance(other, int):
            return Frac(self.x, self.y * other)

    def __rdiv__(self, other): # int/frac
        return Frac(self.y * other, self.x)

    def __pos__(self):
        return self

    def __neg__(self):
        return (-1) * Frac(self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y

    __radd__ = __add__

    __rmul__ = __mul__


class TestFrac(unittest.TestCase):
    def setUp(self):
        self.fracs = (Frac(1, 2), Frac(2, 3), Frac(1, 3), Frac(3, 9), Frac(-1, 3), Frac(3, 9), Frac(1, 5),
                      Frac(3, 15), Frac(0, 1))

    def test_add_frac(self):
        self.add_results = (Frac(7, 6), Frac(1, 1), Frac(2, 3), Frac(0, 1), Frac(0, 1), Frac(8, 15),
                            Frac(2, 5), Frac(1, 5))

        for i in range(0, len(self.fracs) - 1):
            self.assertEqual(self.add_results[i], (self.fracs[i] + self.fracs[i + 1]))

    def test_sub_frac(self):
        self.sub_results = (Frac(-1, 6), Frac(1, 3), Frac(0, 1), Frac(2, 3), Frac(-2, 3), Frac(2, 15),
                            Frac(0, 1), Frac(1, 5))

        for i in range(0, len(self.fracs) - 1):
            self.assertEqual(self.sub_results[i], (self.fracs[i] + self.fracs[i + 1]))

    def tearDown(self):
        pass
