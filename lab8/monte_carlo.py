import random as rd


def calc_pi(n) -> float:
    sq_points = n
    circle_points = 0
    for i in range(sq_points):
        x = 2 * rd.random() - 1
        y = 2 * rd.random() - 1
        if x * x + y * y <= 1:
            circle_points += 1

    return 4 * circle_points / sq_points


print('for n = 100 pi = ' + str(calc_pi(10)))
print('for n = 1000 pi = ' + str(calc_pi(100)))
print('for n = 10000 pi = ' + str(calc_pi(1000)))
print('for n = 100000 pi = ' + str(calc_pi(10000)))
print('for n = 1000000 pi = ' + str(calc_pi(100000)))
print('for n = 10000000 pi = ' + str(calc_pi(1000000)))


