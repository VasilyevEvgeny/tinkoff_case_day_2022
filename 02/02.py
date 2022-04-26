# 01

import time
from itertools import combinations
import math

VERBOSE = False


def is_different(lhs, rhs):
    n_diff = 0
    for i in range(2):
        lhs_digit = lhs % 10
        rhs_digit = rhs % 10
        if VERBOSE:
            print("lhs_digit = {}".format(lhs_digit))
            print("rhs_digit = {}".format(rhs_digit))
        if lhs_digit != rhs_digit:
            n_diff += 1
        lhs = lhs // 10
        rhs = rhs // 10
    if VERBOSE:
        print("n_diff = {}".format(n_diff))

    return n_diff >= 1


def solve():
    i_min, i_max = 10, 20
    length = i_max - i_min
    numbers = [i for i in range(i_min, i_max + 1, 1)]

    # if VERBOSE:
    print("numbers = {}".format(numbers))

    n = 0
    for i in range(2, length + 1, 1):
        for subset in combinations(numbers, i):
            print("subset = {}".format(subset))
            is_ok = True
            for pair in combinations(subset, 2):
                if not is_different(pair[0], pair[1]):
                    is_ok = False
                    break
            if is_ok:
                n += 1

    return n


def analytic_solve():
    i_min, i_max = 10, 20
    n = i_max - i_min
    prob = (8 / 9)**2

    res = 0
    for k in range(2, n + 1, 1):
        res += math.factorial(n) / (math.factorial(n - k) * math.factorial(k - 2))

    return prob * res

if __name__ == '__main__':

    start = time.time()
    solution_1 = solve()
    solution_2 = analytic_solve()
    end = time.time()

    print("\nn = {}".format(solution_1))
    print("\nn_analytic = {}".format(solution_2))
    print("TIME = {:.1f} s".format(end - start))
