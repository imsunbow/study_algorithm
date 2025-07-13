# 백준 12015: 가장 긴 증가하는 부분 수열 2

import sys
import bisect

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = []

for x in a:
    idx = bisect.bisect_left(dp, x) # find location to insert x in dp using bs
    if idx == len(dp): # if x is greater than all elements in dp
        dp.append(x) # append
    else:
        dp[idx] = x # replace the element at idx with x

print(len(dp))  # the length of dp is the length of the longest increasing subsequence
