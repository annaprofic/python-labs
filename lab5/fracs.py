import unittest
import math


def check_frac(frac):
    if not isinstance(frac, (tuple, list)):
        raise ValueError("Value must be list or tuple format.")
    if frac[1] == 0 or len(frac) != 2:
        raise ValueError("Invalid number format.")


def check_data(frac1, frac2):
    check_frac(frac1)
    check_frac(frac2)


def lowest_frac(frac):
    check_frac(frac)
    common_factor = math.gcd(frac[0], frac[1])

    frac[0] = int(frac[0] / common_factor)
    frac[1] = int(frac[1] / common_factor)
    return frac


def add_frac(frac1, frac2):
    check_data(frac1, frac2)

    if frac1[1] == frac2[1]:
        return lowest_frac([frac1[0] + frac2[0], frac1[1]])

    frac3 = [0, 0]
    frac3[1] = (frac1[1] * frac2[1]) // math.gcd(frac1[1], frac2[1])
    frac3[0] = (frac1[0] * (frac3[1] // frac1[1]) +
                frac2[0] * (frac3[1] // frac2[1]))

    return lowest_frac(frac3)


def sub_frac(frac1, frac2):
    check_data(frac1, frac2)

    if frac1[1] == frac2[1]:
        return lowest_frac([frac1[0] - frac2[0], frac1[1]])

    frac3 = [0, 0]
    frac3[1] = (frac1[1] * frac2[1]) // math.gcd(frac1[1], frac2[1])
    frac3[0] = (frac1[0] * (frac3[1] // frac1[1]) -
                frac2[0] * (frac3[1] // frac2[1]))

    return lowest_frac(frac3)


def mul_frac(frac1, frac2):
    check_data(frac1, frac2)
    return lowest_frac([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):
    check_data(frac1, frac2)

    if frac2[0] == 0:
        raise ZeroDivisionError
    return mul_frac(frac1, [frac2[1], frac2[0]])


def cmp_frac(frac1, frac2):
    check_data(frac1, frac2)

    if sub_frac(frac1, frac2) == [0, 1]:
        return 0
    if is_positive(sub_frac(frac1, frac2)):
        return 1
    return -1


def is_positive(frac):
    check_frac(frac)
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)


def is_zero(frac):
    check_frac(frac)
    return frac[0] == 0


def frac2float(frac):
    check_frac(frac)
    return frac[0] / frac[1]


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.fracs = ([1, 2], [2, 3], [1, 3], [3, 9], [-1, 3], [3, 9], [1, 5], [3, 15], [0, 1])
        self.add_results = ([7, 6], [1, 1], [2, 3], [0, 1], [0, 1], [8, 15], [2, 5], [1, 5])
        self.sub_results = ([-1, 6], [1, 3], [0, 1], [2, 3], [-2, 3], [2, 15], [0, 1], [1, 5])
        self.mul_results = ([1, 3], [2, 9], [1, 9], [-1, 9], [-1, 9], [1, 15], [1, 25], [0, 1])
        self.div_results = ([3, 4], [2, 1], [1, 1], [1, -1], [-1, 1], [5, 3], [1, 1])
        self.cmp_results = (-1, 1, 0, 1, -1, 1, 0, 1)

    def test_add_frac(self):
        for i in range(0, len(self.fracs) - 1):
            self.assertEqual(add_frac(self.fracs[i], self.fracs[i + 1]), self.add_results[i])

    def test_sub_frac(self):
        for i in range(0, len(self.fracs) - 1):
            self.assertEqual(sub_frac(self.fracs[i], self.fracs[i + 1]), self.sub_results[i])

    def test_mul_frac(self):
        for i in range(0, len(self.fracs) - 1):
            self.assertEqual(mul_frac(self.fracs[i], self.fracs[i + 1]), self.mul_results[i])

    def test_div_frac(self):
        for i in range(0, len(self.fracs) - 2):
            self.assertEqual(div_frac(self.fracs[i], self.fracs[i + 1]), self.div_results[i])

    def test_cmp_frac(self):
        for i in range(0, len(self.fracs) - 1):
            self.assertEqual(cmp_frac(self.fracs[i], self.fracs[i + 1]), self.cmp_results[i])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([22, 1]), True)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([1, -2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 1]), True)
        self.assertEqual(is_zero([1, 1]), False)
        self.assertEqual(is_zero([-2, 1]), False)

    def test_frac2float(self):
        self.assertEqual(frac2float([0, 2]), 0.0)
        self.assertEqual(frac2float([12, 1]), 12.0)
        self.assertEqual(frac2float([5, 13]), 0.38461538461538464)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()


