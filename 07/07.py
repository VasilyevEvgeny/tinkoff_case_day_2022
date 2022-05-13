from numpy import power, linspace


def solve():
    n = 1000000

    # numerator
    brackets = 0
    for i in range(n):
        brackets += power(i, 1 / 2)
    numerator = n * brackets**2

    # denominator
    brackets = 0
    for i in range(n):
        brackets += power(i, 1 / 3)
    denominator = brackets**3

    return numerator / denominator


def brute_force():
    ps = linspace(2, 1000, 999)
    qs = linspace(2, 1000, 999)
    eps = 0.000001
    for p in ps:
        for q in qs:
            fraction = p / q
            if abs(fraction - 1.0534984801663334) < eps:
                print('p = {}, q = {}, p / q = {}'.format(p, q, fraction))


if __name__ == '__main__':
    solution = solve()
    print(solution)

    brute_force()


#
# Answer
#
# 1
#
