from numpy.linalg import det
from numpy import array
from random import random


def solve():
    c1 = 4
    c2 = 3

    n = 10000000
    res = 0
    for i in range(n):
        x11 = random() * c1
        x22 = random() * c1
        x33 = random() * c1

        x12 = random() * c2
        x13 = random() * c2
        x21 = random() * c2
        x23 = random() * c2
        x31 = random() * c2
        x32 = random() * c2

        arr = array([
            [x11, x12, x13],
            [x21, x22, x23],
            [x31, x32, x33]
        ])

        determinant = det(arr)
        res += determinant

    return res / n


if __name__ == '__main__':
    solution = solve()
    print("\ndet = {}".format(solution))


#
# Answer
#
# 1.25
#


