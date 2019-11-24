import math
import numpy as np


class Frac:
    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Denominator cannot be equal to zero")
        self.x = x
        self.y = y
        self.lowest_frac()

    def lowest_frac(self):
        common_factor = math.gcd(self.x, self.y)
        self.x = int(self.x / common_factor)
        self.y = int(self.y / common_factor)
        return self

    def __str__(self):
        if self.y == 1:
            return f"{self.x}"
        return f"{self.x}/{self.y}"

    def __repr__(self):
        return f"Frac({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Frac):
            return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x

    def __le__(self, other):
        if self.y == other.y:
            return self.x <= other.x

    def __gt__(self, other):
        if self.y == other.y:
            return self.x > other.x

    def __ge__(self, other):
        if self.y == other.y:
            return self.x >= other.x

    def __add__(self, other):
        if not isinstance(other, (Frac, int)):
            raise ValueError("Invalid value format, it must be Frac or Integer value.")

        if isinstance(other, Frac):
            if self.y == other.y:
                self.x += other.x
                return Frac(self.x, self.y)
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
                return Frac(self.x, self.y)
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

    def __truediv__(self, other):  # frac1/frac2, frac/int
        if not isinstance(other, (Frac, int)):
            raise ValueError("Invalid value format, it must be Frac or Integer value.")

        if isinstance(other, Frac):
            return self * Frac(other.y, other.x)

        if isinstance(other, int):
            return Frac(self.x, self.y * other)

    def __rtruediv__(self, other):  # int/frac
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
