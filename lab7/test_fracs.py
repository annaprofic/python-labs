from lab7.fracs import Frac
import unittest


class TestFrac(unittest.TestCase):
    def setUp(self):
        self.frac1 = Frac(1, 2)
        self.frac2 = Frac(2, 3)
        self.frac3 = Frac(1, 3)
        self.frac4 = Frac(3, 9)
        self.frac5 = Frac(-1, 3)

    def test__str__(self):
        self.assertEqual(str(self.frac1), "1/2")
        self.assertEqual(str(self.frac5), "-1/3")

    def test__repr__(self):
        self.assertEqual(repr(self.frac1), "Frac(1, 2)")
        self.assertEqual(repr(self.frac5), "Frac(-1, 3)")

    def test__add__(self):
        self.assertEqual(Frac(7, 6), self.frac1 + self.frac2)
        self.assertEqual(Frac(1, 1), self.frac2 + self.frac3)
        self.assertEqual(Frac(2, 3), self.frac3 + self.frac4)
        self.assertEqual(Frac(0, 1), self.frac4 + self.frac5)

    def test__radd_(self):
        self.assertEqual(Frac(5, 3), 1 + self.frac2)
        self.assertEqual(Frac(5, 3), 2 + self.frac5)

    def test__sub__(self):
        self.assertEqual(Frac(-1, 6), self.frac1 - self.frac2)
        self.assertEqual(Frac(1, 3), self.frac2 - self.frac3)
        self.assertEqual(Frac(0, 1), self.frac3 - self.frac4)
        self.assertEqual(Frac(2, 3), self.frac4 - self.frac5)

    def test__rsub__(self):
        self.assertEqual(Frac(1, 3), 1 - self.frac2)
        self.assertEqual(Frac(-14, 3), -5 - self.frac5)

    def test__mul__(self):
        self.assertEqual(Frac(1, 3), self.frac1 * self.frac2)
        self.assertEqual(Frac(2, 9), self.frac2 * self.frac3)
        self.assertEqual(Frac(1, 9), self.frac3 * self.frac4)

    def test__truediv__(self):
        self.assertEqual(Frac(3, 4), self.frac1 / self.frac2)
        self.assertEqual(Frac(2, 1), self.frac2 / self.frac3)
        self.assertEqual(Frac(1, 1), self.frac3 / self.frac4)

    def test__rtruediv__(self):
        self.assertEqual(Frac(3, 2), 1 / self.frac2)
        self.assertEqual(Frac(6, 1), 2 / self.frac3)
        self.assertEqual(Frac(-30, 1), -10 / self.frac4)

    def test__pos__(self):
        self.assertEqual(self.frac1, +self.frac1)
        self.assertEqual(self.frac2, +self.frac2)

    def test__neg__(self):
        self.assertEqual(Frac(-1, 2), -self.frac1)
        self.assertEqual(Frac(1, 3), -self.frac5)

    def test__invert__(self):
        self.assertEqual(self.frac5, ~Frac(3, -1))
        self.assertEqual(self.frac4, ~Frac(9, 3))

    def test_float(self):
        self.assertEqual(0.5, float(self.frac1))
        self.assertEqual(0.6666666666666666, float(self.frac2))
        self.assertEqual(-0.3333333333333333, float(self.frac5))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
