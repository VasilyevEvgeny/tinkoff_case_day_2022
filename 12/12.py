from numpy import random
from tqdm import tqdm

VERBOSE = False

variants = {'depression': {'prob': 0.8, 'cleaning': 20, 'time': 80},
            'maniac': {'prob': 0.2, 'cleaning': 80, 'time': 20}}


times = []
n = 100000000
for i in tqdm(range(n)):
    cleaning = 100
    time = 0
    step = 0
    while cleaning > 0:
        if VERBOSE:
            print('i = ', step)
        choice = random.choice(['depression', 'maniac'], p=[variants['depression']['prob'], variants['maniac']['prob']])
        if VERBOSE:
            print('...choice = ', choice)
        cleaning -= variants[choice]['cleaning']
        time += variants[choice]['time']
        if VERBOSE:
            print('...cleaning ->', cleaning)
            print('...time ->', time)
        i += 1

    if VERBOSE:
        print('time =', time)

    times.append(time / 100)

print('MEAN TIME:', sum(times) / n, '[hours]')


# n = 1e6
# MEAN TIME: 2.4237815999995296 [hours]
# MEAN TIME: 2.42282199999956 [hours]

# n = 1e7
# MEAN TIME: 2.4217585200513043 [hours]
# MEAN TIME: 2.4217534000511476 [hours]
# MEAN TIME: 2.4227864200512914 [hours]

# n = 1e8
# MEAN TIME: 2.4220289646094875 [hours]


#
# Answer
#
# 2.422
#
