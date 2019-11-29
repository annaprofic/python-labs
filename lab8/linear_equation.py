from math import sqrt


def check_args(a, b, c):
    if not isinstance(a, (int, float)):
        raise ValueError("Bad argument 'a'.")

    if not isinstance(b, (int, float)):
        raise ValueError("Bad arguments 'b'.")

    if not isinstance(c, (int, float)):
        raise ValueError("Bad arguments 'c'.")

    if a == 0:
        raise ValueError("Argument 'a' must be positive.")


def solve1(a, b, c):
    check_args(a, b, c)

    delta = (b * b - 4 * a * c)

    if delta < 0:
        raise ValueError("Result doesn't exist.")

    if delta == 0:
        return "x1 = " + str(round(((-b) / (2 * a)), 2))
    else:
        return "x1 = " + str(round(((-b + sqrt(delta)) / (2 * a)), 2)) +\
               ", x2 = " + str(round(((-b - sqrt(delta)) / (2 * a)), 2))


assert 'x1 = -5.0, x2 = 1.0' == str(solve1(-2, -8, 10))
assert 'x1 = 4.0, x2 = -1.0' == str(solve1(1, -3, -4))
assert 'x1 = 2.0, x2 = -2.0' == str(solve1(1, 0, -4))
assert 'x1 = 7.0, x2 = 0.0' == str(solve1(1, -7, 0))
assert 'x1 = -0.2, x2 = -1.0' == str(solve1(5, 6, 1))
