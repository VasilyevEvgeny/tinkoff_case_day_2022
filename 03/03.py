from numpy import sqrt


def median(a, b, c):
    return sqrt((2 * a**2 + 2 * b**2 - c**2) / 4)


def solve():
    AB = 5
    AC = 6
    BC = 7

    Aa = median(AB, AC, BC)
    Bb = median(AB, BC, AC)
    Cc = median(AC, BC, AB)

    coeff = 2 / 3
    d1, d2, d3 = coeff * Aa, coeff * Bb, coeff * Cc

    return d1**2 + d2**2 + d3**2


if __name__ == '__main__':
    solution = solve()
    print("\ndistance = {}".format(solution))
    print("fraction = {}".format(110 / 3))


#
# Answer
#
# 100 / 3
#
