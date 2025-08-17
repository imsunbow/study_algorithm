import re

pattern = re.compile(r'^(100+1+|01)+$') # if 1,0 appears or 01

s = input().strip()
print("SUBMARINE" if pattern.match(s) else "NOISE")