# 백준 15656 : N과 M (7)

import sys
from itertools import product

input = sys.stdin.readline

n,m = map(int,input().split())
nums = sorted(map(int,input().split()))

for i in product(nums, repeat=m):
    print(*i)