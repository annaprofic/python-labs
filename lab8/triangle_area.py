def check_args(a, b, c):
    if not isinstance(a, (int, float)):
        raise ValueError("Bad argument 'a'.")

    if not isinstance(b, (int, float)):
        raise ValueError("Bad arguments 'b'.")

    if not isinstance(c, (int, float)):
        raise ValueError("Bad arguments 'c'.")

    if (a <= 0) or (b <= 0) or (c <= 0):
        raise ValueError("Arguments 'a', 'b', 'c' must be positive.")

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("The sum of two arguments must be greater or equal to third.")


def heron(a, b, c):

    check_args(a, b, c)

    semi_perimeter = (a + b + c) / 2
    result = round(((semi_perimeter *
                     (semi_perimeter - a) *
                     (semi_perimeter - b) *
                     (semi_perimeter - c)) ** 0.5), 2)

    return result


assert '9.8' == str(heron(4, 5, 7))
assert '8.79' == str(heron(9, 3, 7))
assert '5.56' == str(heron(2, 6, 7))
assert '0.5' == str(heron(1, 1.4142, 1))
assert '12.79' == str(heron(4, 6.5, 7))
