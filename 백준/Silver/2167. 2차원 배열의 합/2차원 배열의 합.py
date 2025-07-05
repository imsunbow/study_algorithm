#백준 2167: 2차원 배열의 합

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
k = int(input())

sum_lst = [list(map(int,input().split())) for _ in range(k)]

dp = [[0 for i in range(m+1)] for i in range(n+1)]

# make accumulated sum table 
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + lst[i-1][j-1]

# query handling
for x1, y1, x2, y2 in sum_lst:
    res = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(res)
      