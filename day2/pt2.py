import os
import re

os.chdir(os.path.dirname(__file__))

def xor(a,b):
    return (a or b) and not (a and b)

total_count = 0
with open('input', 'r') as fid:
    while True:
        line = fid.readline().strip()
        if not line:
            break
        
        m = re.match(r'(?P<pos1>\d+)-(?P<pos2>\d+) (?P<char>.): (?P<password>.*)', line)
        if not m:
            print(f'Warning: {line!r} did not match!')
        
        if xor(m['password'][int(m['pos1'])-1]==m['char'], m['password'][int(m['pos2'])-1]==m['char']):
            total_count+=1

print(total_count)
