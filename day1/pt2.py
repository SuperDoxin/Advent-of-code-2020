import os
from bisect import bisect_left, bisect_right

os.chdir(os.path.dirname(__file__))

numbers = []
with open('input', 'r') as fid:
    while True:
        line = fid.readline().strip()
        if not line:
            break
        numbers.append(int(line))

numbers.sort()
print(f'loaded {len(numbers)} numbers')

for i, n1 in enumerate(numbers):
    n2_candidates = numbers[:bisect_left(numbers, 2020-n1)]
    for j,n2 in enumerate(n2_candidates):
        n3_candidates = numbers[:bisect_right(numbers, 2020-n1-n2)]
        for n3 in n3_candidates:
            if n1+n2+n3==2020:
                print(f'{n1}+{n2}+{n3} = {n1+n2+n3}')
                print(f'{n1}*{n2}*{n3} = {n1*n2*n3}')
                raise SystemExit()
print('No solution found.')
