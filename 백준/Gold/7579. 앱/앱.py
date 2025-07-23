# 백준 7579: 앱

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

MAX_COST = sum(cost)
dp = [0] * (MAX_COST + 1)

for i in range(n):
    temp_m = memory[i]
    temp_c = cost[i]
    for j in range(MAX_COST, temp_c - 1, -1):
        dp[j] = max(dp[j], dp[j - temp_c] + temp_m)
        
for i in range(MAX_COST + 1):
    if dp[i] >= m:
        print(i)
        break