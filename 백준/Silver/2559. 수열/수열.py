#백준 2559: 수열

import sys
input = sys.stdin.readline

n,k = map(int, input().split())
temp = list(map(int, input().split()))

current_sum = sum(temp[:k]) 
max_sum = current_sum

for i in range(k, n):
    current_sum += temp[i] - temp[i-k]
    max_sum = max(max_sum, current_sum)
print(max_sum)