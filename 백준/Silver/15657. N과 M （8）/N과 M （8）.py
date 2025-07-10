# 백준 15657 : N과 M (8)

import sys
from itertools import product

input = sys.stdin.readline

n,m = map(int, input().split())
nums = sorted(map(int, input().split()))

for p in product(nums, repeat=m):
    if all(p[i] <= p[i+1] for i in range(m-1)): # Ensure non-decreasing order
        print(*p)