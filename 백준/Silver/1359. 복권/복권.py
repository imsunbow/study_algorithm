# 백준 1359 : 복권

from itertools import combinations
from math import comb

n, m, k = map(int, input().split())

winning = 0

for case in combinations(range(n), m):
    cnt = sum(1 for i in case if i < m)  
    if cnt >= k:
        winning += 1

total_combinations = comb(n, m)  
print(winning / total_combinations)
