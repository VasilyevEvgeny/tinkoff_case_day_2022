from numpy import linspace, zeros, array, append
from numba import jit
from random import shuffle

from matplotlib import pyplot as plt


@jit(nopython=True)
def is_ok(a, b, c, eps):
    return abs((a / 4 + b / 3 + c / 2) - (-1 / 2)) < eps and \
           abs((a + b + c) - (-1)) < eps


@jit(nopython=True)
def find_coefficients():
    aa = linspace(-1, 1, 500)
    bb = linspace(-1, 1, 500)
    cc = linspace(-1, 1, 500)

    eps = 0.002
    res = zeros(shape=(0,))
    for a in aa:
        for b in bb:
            for c in cc:
                if is_ok(a, b, c, eps):
                    res = append(res, array([a, b, c]))

    return res


def solve():
    arr = find_coefficients()
    pool = []
    for i in range(0, len(arr), 3):
        pool.append([arr[i], arr[i + 1], arr[i + 2]])

    shuffle(pool)

    n_points = 10
    xs = linspace(0, 1, n_points)
    fs = []
    n_top = 5
    for i in range(n_top):
        func = []
        for x in xs:
            f = pool[i][0] * x**3 + pool[i][1] * x**2 + pool[i][2] * x + 1
            func.append(f)
        fs.append(func)

    plt.figure()
    for i in range(n_top):
        plt.plot(xs, fs[i])

    plt.axvline(x=0.5, c='black', ls=':')
    plt.axhline(y=0.5, c='black', ls=':')

    plt.xlabel('$x$', fontsize=12)
    plt.ylabel('$f(x)$', fontsize=12)

    plt.savefig('polynom.png', dpi=200)
    plt.close()


if __name__ == '__main__':
    solve()


#
# Answer
#
# 0.50
#


