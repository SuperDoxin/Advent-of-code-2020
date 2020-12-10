import os
import re

os.chdir(os.path.dirname(__file__))

with open('input', 'r') as fid:
    lines = fid.readlines()

lines = [line.strip() for line in lines if line.strip()]

count = 0
x = 0
for line in lines:
    char = line[x % len(line)]
    x+=3
    if char=='#':
        count+=1

print(count)
