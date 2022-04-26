# 01

import time

VERBOSE = True


def is_all_digits_in_remainders(arr):
    return (1 in arr) and (2 in arr) and (3 in arr) and \
           (4 in arr) and (5 in arr) and (6 in arr) and \
           (7 in arr) and (8 in arr) and (9 in arr)


def solve():
    result = None
    n = 100
    for i in range(2, n + 1, 1):
        if VERBOSE:
            print("i = {}".format(i))
        remainders = []
        for j in range(1, i, 1):
            remainder = i % j
            if VERBOSE:
                print("...{} % {} = {}".format(i, j, remainder))
            if (remainder not in remainders) and len(str(remainder)) == 1 and remainder:
                remainders.append(remainder)
        if VERBOSE:
            print("...remainders = {}".format(remainders))
            print("...OK = {}".format(is_all_digits_in_remainders(remainders)))

        if not is_all_digits_in_remainders(remainders):
            result = i

    return result


if __name__ == '__main__':

    start = time.time()
    solution = solve()
    end = time.time()

    print("\nn_max = {}".format(solution))
    print("TIME = {:.1f} s".format(end - start))


#
# Answer
#
# 18
#
