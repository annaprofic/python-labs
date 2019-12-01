def check_args(a, b, c):
    if not isinstance(a, (int, float)):
        raise ValueError("Bad argument 'a'.")

    if not isinstance(b, (int, float)):
        raise ValueError("Bad arguments 'b'.")

    if not isinstance(c, (int, float)):
        raise ValueError("Bad arguments 'c'.")

    if a == 0 and b == 0:
        raise ValueError("Arguments 'a', 'b' must be positive.")


def solve1(a, b, c):
    check_args(a, b, c)

    if a == 0 and b != 0:
        return f"{-c / b}"
    if a != 0 and b == 0:
        return f"{-c / a}"
    else:
        return f" {- (a / b)} * x + {- (c / b)}"


assert '9.0 * x + 2.0' == solve1(63, -7, 14)
assert '22.0' == str(solve1(0, 0.5, -11))

