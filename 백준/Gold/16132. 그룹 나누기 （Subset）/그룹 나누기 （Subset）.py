import sys

input = sys.stdin.readline

n = int(input())
total_way = n * (n + 1) // 2

if total_way % 2 != 0:
    print(0)
else:
    total_way //= 2
    dp = [0] * (total_way + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(total_way, i - 1, -1):
            dp[j] += dp[j - i]

    print(dp[total_way] // 2)