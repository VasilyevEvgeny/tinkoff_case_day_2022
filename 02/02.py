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
    i_min, i_max = 10000, 99999
    length = i_max - i_min
    numbers = [i for i in range(i_min, i_max + 1, 1)]

    # if VERBOSE:
    print("numbers = {}".format(numbers))

    res = 0
    for i in range(length, 1, -1):
        subsets = list(combinations(numbers, i))
        for subset in subsets:
            print("len of subset = {}".format(i))
            is_ok = True
            pairs = list(combinations(subset, 2))
            for pair in pairs:
                if not is_different(pair[0], pair[1]):
                    is_ok = False
                    break
            if is_ok:
                print("i_max = {}".format(i))
                res = i
                break

    return res


def solve_analytically():
    return 9 * 10 * 10 * 9 * 9


if __name__ == '__main__':

    start = time.time()
    # solution = solve()
    solution = solve_analytically()
    end = time.time()

    print("\nn = {}".format(solution))
    print("TIME = {:.1f} s".format(end - start))

#
# Answer
#
# 72900
#
