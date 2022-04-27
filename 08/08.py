from matplotlib import pyplot as plt
from numpy import linspace, sqrt


def f_parabola(x):
    return x**2


def f_circle_up(x, b):
    return sqrt(1 - x**2) + b


def f_circle_down(x, b):
    return -sqrt(1 - x**2) + b


def plot(b):
    n_points = 1000

    xs_parabola = linspace(-2, 2, n_points)
    parabola = []
    for x in xs_parabola:
        parabola.append(f_parabola(x))

    xs_circle = linspace(-1, 1, n_points)
    circle_up, circle_down = [], []
    for x in xs_circle:
        circle_up.append(f_circle_up(x, b))
        circle_down.append(f_circle_down(x, b))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    plt.plot(xs_parabola, parabola, c='red')
    plt.plot(xs_circle, circle_up, c='blue')
    plt.plot(xs_circle, circle_down, c='blue')
    plt.axvline(x=0, c='black', ls=':')
    plt.axhline(y=0, c='black', ls=':')
    plt.axhline(y=b, c='green', ls=':')

    # grid
    plt.axvline(x=-1, c='gray', ls=':', alpha=0.5)
    plt.axvline(x=1, c='gray', ls=':', alpha=0.5)
    plt.axhline(y=1, c='gray', ls=':', alpha=0.5)
    plt.axhline(y=2, c='gray', ls=':', alpha=0.5)

    plt.xlabel('$x$', fontsize=12)
    plt.ylabel('$f(x)$', fontsize=12)
    plt.savefig('graphics.png', bbox_inches='tight', dpi=200)
    plt.close()


def solve():
    b = 1.25
    plot(b)


if __name__ == '__main__':
    solve()


#
# Answer
#
# 1.25
#
