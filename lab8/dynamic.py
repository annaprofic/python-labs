def check_args(i, j):
    if i < 0 or j < 0:
        raise ValueError("Arguments must be greater or equal to 0.")


values = {(0, 0): 0.5}


def p(i, j):
    check_args(i, j)

    if (i, j) in values.keys():
        return values.get((i, j))

    if (i > 0) and (j == 0):
        return 0.0
    elif (i == 0) and (j > 0):
        return 1.0
    elif (i > 0) and (j > 0):
        values[(i, j)] = 0.5 * (p(i - 1, j) + p(i, j - 1))
        return values.get((i, j))


assert p(1, 0) == 0.0
assert p(0, 1) == 1.0
assert p(0, 0) == 0.5
assert p(1, 8) == 0.99609375
assert p(2, 9) == 0.9892578125
assert p(3, 2) == 0.3125
assert p(3, 1) == 0.125
assert p(7, 3) == 0.08984375

# wersja dynamiczna jest szybsza od rekurencyjnej, poniewaz przechowuje juz znane wyniki i
# nie traci na tym, aby je obliczyc - funkcja po prostu je zwraca z slownika
