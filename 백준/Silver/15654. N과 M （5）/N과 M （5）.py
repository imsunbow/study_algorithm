# 백준 15654 : N과 M (5)

import sys
from itertools import permutations
input = sys.stdin.readline

n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))

res = permutations(arr, m)
for i in res:
    print(*i)