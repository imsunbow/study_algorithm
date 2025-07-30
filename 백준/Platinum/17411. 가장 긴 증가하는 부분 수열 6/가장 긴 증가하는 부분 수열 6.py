import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

MOD = 10 ** 9 + 7

n = int(input())
arr = list(map(int, input().split()))

dp = []
lengths = []

for x in arr:
    idx = bisect_left(dp, x)
    if idx == len(dp):
        dp.append(x)
    else:
        dp[idx] = x
    lengths.append(idx + 1)

max_len = len(dp)

num = [[] for _ in range(max_len + 2)]
prefix_sum = [[] for _ in range(max_len + 2)]

for i in range(1, max_len + 1):
    prefix_sum[i].append(0)

for i in reversed(range(n)):
    val = arr[i]
    l = lengths[i]

    if l == max_len:
        cnt = 1
    else:
        idx = bisect_right(num[l + 1], val)
        total = prefix_sum[l + 1][-1]
        subtract = prefix_sum[l + 1][idx] if idx < len(prefix_sum[l + 1]) else 0
        cnt = (total - subtract) % MOD

    num[l].append(val)
    prefix_sum[l].append((prefix_sum[l][-1] + cnt) % MOD)

print(max_len, prefix_sum[1][-1])