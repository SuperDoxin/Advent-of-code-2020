import os
import re

os.chdir(os.path.dirname(__file__))

total_count = 0
with open('input', 'r') as fid:
    while True:
        line = fid.readline().strip()
        if not line:
            break
        
        m = re.match(r'(?P<min>\d+)-(?P<max>\d+) (?P<char>.): (?P<password>.*)', line)
        if not m:
            print(f'Warning: {line!r} did not match!')
        
        count = m['password'].count(m['char'])
        if count <= int(m['max']) and count >= int(m['min']):
            total_count+=1

print(total_count)
