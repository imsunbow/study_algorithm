import sys
from math import comb

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

remainder_count = [0] * m
prefix_sum = 0

for i in range(n):
    prefix_sum += lst[i]
    remainder_count[prefix_sum % m] += 1 # count prefix sum % m
    
result = remainder_count[0]

for count in remainder_count:
    result += comb(count, 2)
    
print(result)