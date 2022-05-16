from itertools import permutations
from numpy import zeros, full


VERBOSE = False

answers = []

results = {}


def check_results(last_row, cur_res):
    last_row = list(last_row)
    last_row.remove('#')
    s = 0
    for e in last_row:
        s += int(e)
    if s not in results.keys():
        results.update({s: cur_res})


def set_result(arr, i, j, points):
    grate_pos = list(arr[i, :]).index('#')
    j += grate_pos + 1
    arr[i, j] = points
    if arr[i, j] == '3':
        arr[j, i] = '0'
    elif arr[i, j] == '1':
        arr[j, i] = '1'
    else:
        arr[j, i] = '3'

    if VERBOSE:
        print('in set_result. arr:\n', arr)

    return arr


def get_all_correct_variants(arr, i):
    row_init = arr[i, :]
    if VERBOSE:
        print('row_init = ', row_init)
    row = []
    for e in row_init:
        if e != '#':
            row.append(e)

    if VERBOSE:
        print('row = ', row)

    cur_sum = 0
    free_positions = 5
    for e in row:
        if e.isnumeric():
            cur_sum += int(e)
            free_positions -= 1

    remainder = 6 - cur_sum
    if cur_sum > 6:
        return None
        # raise Exception('cur_sum > 6!')

    if VERBOSE:
        print('cur_sum =', cur_sum)
        print('remainder = ', remainder)
        print('free_positions = ', free_positions)

    raw_values = None
    if remainder == 0:
        if free_positions == 1:
            raw_values = [[0]]
        elif free_positions == 2:
            raw_values = [[0, 0]]
        elif free_positions == 3:
            raw_values = [[0, 0, 0]]
        elif free_positions == 4:
            raw_values = [[0, 0, 0, 0]]
        else:
            raw_values = [[0, 0, 0, 0, 0]]
    elif remainder == 1:
        if free_positions == 1:
            raw_values = [[1]]
        elif free_positions == 2:
            raw_values = [[1, 0]]
        elif free_positions == 3:
            raw_values = [[1, 0, 0]]
        elif free_positions == 4:
            raw_values = [[1, 0, 0, 0]]
        else:
            raw_values = [[1, 0, 0, 0, 0]]
    elif remainder == 2:
        if free_positions == 1:
            return None
            # raise Exception('remainder = 2, free_positions == 1!')
        elif free_positions == 2:
            raw_values = [[1, 1]]
        elif free_positions == 3:
            raw_values = [[1, 1, 0]]
        elif free_positions == 4:
            raw_values = [[1, 1, 0, 0]]
        else:
            raw_values = [[1, 1, 0, 0, 0]]
    elif remainder == 3:
        if free_positions == 1:
            raw_values = [[3]]
        elif free_positions == 2:
            raw_values = [[3, 0]]
        elif free_positions == 3:
            raw_values = [[1, 1, 1], [3, 0, 0]]
        elif free_positions == 4:
            raw_values = [[3, 0, 0, 0], [1, 1, 1, 0]]
        else:
            raw_values = [[3, 0, 0, 0, 0], [1, 1, 1, 0, 0]]
    elif remainder == 4:
        if free_positions == 1:
            return None
            # raise Exception('remainder = 4, free_positions == 1!')
        elif free_positions == 2:
            raw_values = [[3, 1]]
        elif free_positions == 3:
            raw_values = [[3, 1, 0]]
        elif free_positions == 4:
            raw_values = [[3, 1, 0, 0], [1, 1, 1, 1]]
        else:
            raw_values = [[3, 1, 0, 0, 0], [1, 1, 1, 1, 0]]
    elif remainder == 5:
        if free_positions == 1:
            return None
            # raise Exception('remainder = 5, free_positions == 1!')
        elif free_positions == 2:
            return None
            # raise Exception('remainder = 5, free_positions == 2!')
        elif free_positions == 3:
            raw_values = [[3, 1, 1]]
        elif free_positions == 4:
            raw_values = [[3, 1, 1, 0]]
        else:
            raw_values = [[3, 1, 1, 0, 0], [1, 1, 1, 1, 1]]
    elif remainder == 6:
        if free_positions == 1:
            return None
            # raise Exception('remainder = 6, free_positions == 1!')
        elif free_positions == 2:
            raw_values = [[3, 3]]
        elif free_positions == 3:
            raw_values = [[3, 3, 0]]
        elif free_positions == 4:
            raw_values = [[3, 3, 0, 0], [3, 1, 1, 1]]
        else:
            raw_values = [[3, 3, 0, 0, 0], [3, 1, 1, 1, 0]]

    if VERBOSE:
        print('raw_values = ', raw_values)

    values = []
    for i in range(len(raw_values)):
        perm = list(permutations(raw_values[i]))
        for e in perm:
            if e not in values:
                values.append(e)

    return values


def process(results, variants, i_row):
    results_cur = results.copy()

    if VERBOSE:
        print('==================================')
        print('results = \n', results_cur)
        print('variants = \n', variants)
        print('i_row =', i_row)

    # if i_row == 5:
    #     if VERBOSE:
    #         print('i_row = 5!!!!!!!!!')
    #     print(results_cur[-1, :])
    #     i_row -= 1
    #     return
    # else:

    if variants is None:
        if VERBOSE:
            print('bad branch!')
        return

    for variant in variants:
        results_for_var = results_cur.copy()
        if VERBOSE:
            print('results = \n', results_for_var)
            print('variant: ', variant)
        for i_col, res in enumerate(variant):
            if VERBOSE:
                print('set_result: i_row =', i_row, ', i_col = ', i_col, ', res = ', res)
            set_result(results_for_var, i_row, i_col, res)

        if i_row < 4:
            process(results_for_var, get_all_correct_variants(results_for_var, i_row + 1), i_row + 1)
        else:
            answers.append(results_for_var[-1, :])
            print('FINAL:\nlast_row:\n', results_for_var[-1, :])
            print('all results:\n', results_for_var)
            check_results(results_for_var[-1, :], results_for_var)


def solve():
    n = 6
    results = full((n, n), '-')
    for i in range(n):
        results[i, i] = '#'

    process(results, get_all_correct_variants(results, 0), 0)

    print('number of answers:', len(answers))
    answers_short = []
    for line in answers:
        if list(line) not in answers_short:
            answers_short.append(list(line))

    for e in answers_short:
        print(e)
    print('number of answers_short:', len(answers_short))

    for i in range(len(answers_short)):
        answers_short[i] = answers_short[i][:-1]
        answers_short[i].sort()

    answers_final = []
    for e in answers_short:
        if e not in answers_final:
            answers_final.append(e)

    for e in answers_final:
        print(e)
    print('number of answers_final:', len(answers_final))

    points = 0
    for i in range(len(answers_final)):
        for j in range(len(answers_final[0])):
            points += int(answers_final[i][j])
    print('ANSWER:', points)


if __name__ == '__main__':
    solve()

    print(results)

#
# Answer
#
# 66
#
