import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

homes = [(r, c) for r in range(n) for c in range(n) if city[r][c] == 1]
shops = [(r, c) for r in range(n) for c in range(n) if city[r][c] == 2]

best = float('inf')

for comb in combinations(shops, m): 
    total = 0
    for hr, hc in homes:
        d = min(abs(hr - sr) + abs(hc - sc) for sr, sc in comb)
        total += d
        if total >= best:  
            break
    if total < best:
        best = total

print(best)