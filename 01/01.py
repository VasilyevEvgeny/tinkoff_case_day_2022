# 01

from tqdm import tqdm
from numba import jit

verbose = True


@jit(nopython=True)
def is_all_digits_in_remainders(arr):
    return (1 in arr) and (2 in arr) and (3 in arr) and \
           (4 in arr) and (5 in arr) and (6 in arr) and \
           (7 in arr) and (8 in arr) and (9 in arr)


@jit(nopython=True)
def solve():
    result = []
    n = 10000
    for i in range(1, n + 1, 1):
        # if verbose:
        #     print("i = {}".format(i))
        remainders = []
        for j in range(1, i + 1):
            remainder = n % j
            if (remainder not in remainders) and len(str(remainder)) == 1:
                remainders.append(remainder)
        # if verbose:
        #     print("...remainders = {}".format(remainders))
        #     print("...OK = {}".format(is_all_digits_in_remainders(remainders)))

        if is_all_digits_in_remainders(remainders):
            result.append(i)

    return result


if __name__ == '__main__':
    solution = solve()
    print(solution)
