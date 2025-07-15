# 백준 13136: DNTA

import sys
input = sys.stdin.readline

r,c,n = map(int,input().split())
max_width = r//n+1 if r%n else r//n
max_length = c//n+1 if c%n else c//n

res = max_width * max_length

print(res)
