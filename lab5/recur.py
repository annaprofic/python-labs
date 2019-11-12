def fibonacci_rec(n2):
    if n2 == 0:
        return 0
    if n2 == 1:
        return 1
    return fibonacci_rec(n2 - 1) + fibonacci_rec(n2 - 2)


def factorial_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return n
    return n * factorial_rec(n - 1)

