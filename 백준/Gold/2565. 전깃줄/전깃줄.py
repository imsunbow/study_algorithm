# 백준 2565: 전깃줄

import sys
input = sys.stdin.readline

n = int(input())
lst = []
dp = [True] * n

for i in range(n):
    a,b = map(int, input().split())
    lst.append([a,b])

# main idea :
# 1) sort by a -> 2) find longest increasing subsequence on b 

lst.sort()

for i in range(n):
    for j in range(0,i):
        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i], dp[j] + 1) # LIS

print(n - max(dp))  # print the minimum number of wires to remove