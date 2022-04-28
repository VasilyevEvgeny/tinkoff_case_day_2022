from numpy import argmax
import numpy as np

VERBOSE = False


def are_equal(sweets):
    return sweets.count(sweets[0]) == len(sweets)


def do(sweets, i):
    sweets[i] -= 4
    sweets[(i - 1 + 6) % 6] += 1
    sweets[(i + 1) % 6] += 1
    sweets[(i + 3) % 6] += 1

    return sweets


def solve():
    threshold = 4
    success = 0

    print('\n')
    for n in range(1, 1001, 1):
        if VERBOSE:
            print('n =', n)

        sweets = [n, 0, 0, 0, 0, 0]

        while True:
            if VERBOSE:
                print('...sweets =', sweets)

            if are_equal(sweets):
                if VERBOSE:
                    print('...branch are_equal')
                success += 1
                break
            else:
                if VERBOSE:
                    print('...branch are not equal')
                if np.max(sweets) >= threshold:
                    if VERBOSE:
                        print('......branch np.max(sweets) >= threshold')
                    i_argmax = argmax(sweets)
                    sweets = do(sweets, i_argmax)
                else:
                    if VERBOSE:
                        print('......branch !(np.max(sweets) >= threshold)')
                    break

    print('success =', success)


if __name__ == '__main__':
    solve()


#
# Answer
#
# 35
#
