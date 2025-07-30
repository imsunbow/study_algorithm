import sys
from math import hypot

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = hypot(cx - x1, cy - y1)
        d2 = hypot(cx - x2, cy - y2)
        
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1
            
    print(cnt)