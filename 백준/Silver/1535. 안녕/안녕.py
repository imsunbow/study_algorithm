import sys
input = sys.stdin.readline
n = int(input())
hp = list(map(int, input().split()))
pleasure = list(map(int, input().split()))
dp = [0] * 101  
for i in range(n):
    for j in range(99, hp[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - hp[i]] + pleasure[i])
print(max(dp))          