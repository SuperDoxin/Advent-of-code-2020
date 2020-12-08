import os
os.chdir(os.path.dirname(__file__))

numbers = set()
with open('input', 'r') as fid:
    while True:
        line = fid.readline().strip()
        if not line:
            break
        numbers.add(int(line))

print(f'loaded {len(numbers)} numbers')
for number in numbers:
    other_number = 2020-number
    if other_number < 0:
        continue
    if other_number not in numbers:
        continue
    print(f'{number} + {other_number} = {number+other_number}')
    print(f'{number} * {other_number} = {number*other_number}')
    break
else:
    print('No solution found')
