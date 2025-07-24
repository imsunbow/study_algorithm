# 백준 1 2 3 더하기 4 

import sys
input = sys.stdin.readline

dp = [1] * 10001 # reset dp data

for i in range(2,10001): # make 2
    dp[i] += dp[i - 2]
    
for i in range(3,10001): # make 3 (* index should be from 3 )
    dp[i] += dp[i - 3]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])        