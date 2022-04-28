from numpy.linalg import matrix_rank
from numpy import full, random
from itertools import permutations
import time

VERBOSE = False


class Solver:
    def __init__(self):
        self.__n = 5
        self.__permutations = self.__get_possible_permutations()

        self.__k_rank_3 = 0
        self.__k_rank_all = 0
        self.__max = 32**5

        self.__rank3matrices = []

    @staticmethod
    def __get_possible_permutations():
        all_perms = []
        for e in [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 1],
                  [0, 0, 1, 1, 1],
                  [0, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1]]:
            cur = list(permutations(e))
            all_perms += cur

        all_perms_short = []
        for e in all_perms:
            if e not in all_perms_short:
                all_perms_short.append(e)

        return all_perms_short

    @staticmethod
    def __set_row(matrix, i_row, permutation):
        if VERBOSE:
            print('set_row:')
            print('matrix =\n', matrix)
            print('i_row =', i_row)
            print('permutation =', permutation)

        for i_col in range(len(permutation)):
            matrix[i_row, i_col] = permutation[i_col]

    def __process(self, matrix, i_row):
        matrix_cur = matrix.copy()

        if VERBOSE:
            print('matrix_cur =\n', matrix_cur)
            print('i_row =', i_row)

        if i_row == self.__n:
            rank = matrix_rank(matrix_cur)
            self.__k_rank_all += 1
            if rank == 3:
                self.__k_rank_3 += 1
                # self.__rank3matrices.append(matrix_cur)
                if VERBOSE:
                    print('rank = 3!')
                    print('k ->', self.__k_rank_3)
            if not self.__k_rank_all % 100000:
                print('k_rank_3 = {:d}, rel = {:04.2f}%'.format(self.__k_rank_3, self.__k_rank_all / self.__max * 100))
        else:
            for perm in self.__permutations:
                self.__set_row(matrix_cur, i_row, perm)
                self.__process(matrix_cur, i_row + 1)

    def solve(self):
        matrix = full((self.__n, self.__n), -1)
        self.__process(matrix, 0)

        print('MATRICES =\n', self.__rank3matrices)
        print('K =', self.__k_rank_3)


if __name__ == '__main__':
    solver = Solver()

    start = time.time()
    solver.solve()
    end = time.time()
    print("TIME = {:.1f} s".format(end - start))


#
# Answer
#
# 3159750
#
