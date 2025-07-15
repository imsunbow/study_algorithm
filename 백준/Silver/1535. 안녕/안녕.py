# # sol 1) using combination library

# import sys
# from itertools import combinations

# input = sys.stdin.readline
# n = int(input())
# hp = list(map(int, input().split()))
# pleasure = list(map(int, input().split()))

# lst = [(hp[i], pleasure[i]) for i in range(n)] # list comprehension

# max_pleasure = 0
# for i in range(1, n + 1):
#     for comb in combinations(lst, i):
#         hp_temp = sum(x[0] for x in comb)
#         pleasure_temp = sum(x[1] for x in comb)
#         if hp_temp < 100:
#             max_pleasure = max(max_pleasure, pleasure_temp)

# print(max_pleasure)

#sol 2) dp

import sys

input = sys.stdin.readline

n = int(input())
hp = list(map(int, input().split()))
pleasure = list(map(int, input().split()))

dp = [0] * 101  # 체력 소모 0~100까지

for i in range(n):
    for j in range(99, hp[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - hp[i]] + pleasure[i])

print(max(dp))
          