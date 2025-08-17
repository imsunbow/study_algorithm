import re

pattern = re.compile(r'^(100+1+|01)+$')

for _ in range(int(input())):
    s = input().strip()
    print("YES" if pattern.match(s) else "NO")