# 백준 14786: Ax + Bsinx = C

import math

a,b,c = map(int, input().split())

def f(x):
    return a*x + b*math.sin(x) - c

l,r = 0,100000

for _ in range(100000):
    mid = (l + r) / 2
    if f(mid) < 0:
        l = mid
    else:
        r = mid

print(mid)
