from matplotlib import pyplot as plt
from numpy import linspace, sqrt


def f_parabola(x):
    return x**2 - 2 * x - 6


def f_hyperbola_up(x):
    return sqrt(x**2 - 1)


def f_hyperbola_down(x):
    return -sqrt(x**2 - 1)


def f_circle_up(x, a, b, r):
    return sqrt(r**2 - (x - a)**2) + b


def f_circle_down(x, a, b, r):
    return -sqrt(r**2 - (x - a)**2) + b


def plot():
    n_points = 1000

    xs_parabola = linspace(-4, 6, n_points)
    parabola = []
    for x in xs_parabola:
        parabola.append(f_parabola(x))

    xs_hyperbola_left = linspace(-5, -1, n_points)
    xs_hyperbola_right = linspace(1, 6, n_points)
    hyperbola_left_up, hyperbola_left_down, hyperbola_right_up, hyperbola_right_down = [], [], [], []
    for x in xs_hyperbola_left:
        hyperbola_left_up.append(f_hyperbola_up(x))
        hyperbola_left_down.append(f_hyperbola_down(x))
    for x in xs_hyperbola_right:
        hyperbola_right_up.append(f_hyperbola_up(x))
        hyperbola_right_down.append(f_hyperbola_down(x))

    a = 2
    b = 1
    r = 4
    xs_circle = linspace(a - r, a + r, n_points)
    circle_up, circle_down = [], []
    for x in xs_circle:
        circle_up.append(f_circle_up(x, a, b, r))
        circle_down.append(f_circle_down(x, a, b, r))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal', adjustable='box')
    plt.plot(xs_parabola, parabola, c='red', lw=1)
    plt.plot(xs_hyperbola_left, hyperbola_left_up, c='blue', lw=1)
    plt.plot(xs_hyperbola_left, hyperbola_left_down, c='blue', lw=1)
    plt.plot(xs_hyperbola_right, hyperbola_right_up, c='blue', lw=1)
    plt.plot(xs_hyperbola_right, hyperbola_right_down, c='blue', lw=1)
    plt.plot(xs_circle, circle_up, c='black', lw=1)
    plt.plot(xs_circle, circle_down, c='black', lw=1)

    plt.axvline(x=a, c='black', ls=':')
    plt.axhline(y=b, c='black', ls=':')

    # grid
    for i in range(-3, 6, 1):
        plt.axvline(x=i, c='gray', ls=':', lw=0.5, alpha=0.5)

    for i in range(-4, 7, 1):
        plt.axhline(y=i, c='gray', ls=':', lw=0.5, alpha=0.5)

    plt.xlim([-7, 7])

    plt.xlabel('$x$', fontsize=12)
    plt.ylabel('$f(x)$', fontsize=12)
    plt.savefig('graphics.png', bbox_inches='tight', dpi=200)
    plt.close()


def solve():
    plot()


if __name__ == '__main__':
    solve()


#
# Answer
#
# 4
#
