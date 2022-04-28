from numpy import random
from tqdm import tqdm

VERBOSE = False


def solve():
    n1, n2 = 0, 0

    print('\n')
    iterations = 1000000
    for i in tqdm(range(iterations)):
        command_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        command_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        if VERBOSE:
            print('\ni =', i)

        while len(command_1) and len(command_2):
            e1, e2 = command_1[0], command_2[0]
            name1 = '...command1_{}'.format(str(e1))
            name2 = '...command2_{}'.format(str(e2))
            p1, p2 = e1 / (e1 + e2), e2 / (e1 + e2)

            if VERBOSE:
                print('...e1 =', e1, ' e2 =', e2)
                print('...name1 =', name1, ' name2 =', name2)
                print('...p1 =', p1, ' p2 =', p2)

            choice = random.choice([name1, name2], p=[p1, p2])

            if VERBOSE:
                print('...choice ->', choice)

            if choice == name1:
                command_2.pop(0)
            else:
                command_1.pop(0)

            if VERBOSE:
                print('command_1 =', command_1)
                print('command_2 =', command_2)

            if not len(command_1) or not len(command_2):
                break

        if not len(command_1):
            n2 += 1
        elif not len(command_2):
            n1 += 1
        else:
            raise Exception('Wrong branch!')

        if VERBOSE:
            print('n1 ->', n1)
            print('n2 ->', n2)

    print('Prob of command_1 wins =', n1 / (n1 + n2))


if __name__ == '__main__':
    solve()

#
# Answer
#
# 0.50
#
