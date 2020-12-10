import os
import re

os.chdir(os.path.dirname(__file__))

with open('input', 'r') as fid:
    lines = fid.readlines()

lines = [line.strip() for line in lines if line.strip()]

slopes = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

total_result = 1
for slope in slopes:
    count = 0
    x = 0
    for line in lines[::slope[1]]:
        char = line[x % len(line)]
        x+=slope[0]
        if char=='#':
            count+=1
    
    total_result *= count

print(total_result)
