n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort()

dp = [float('inf')] * (k + 1)
dp[0] = 0

for coin in coins:
    for j in range(coin, k+1):
        dp[j] = min(dp[j], dp[j-coin] + 1)

print(dp[k] if dp[k] != float('inf') else -1)