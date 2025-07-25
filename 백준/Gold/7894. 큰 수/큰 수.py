import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):    
    n = int(input())
    if n == 0 or n == 1:
        print(1)
    else:
        log_sum = sum(math.log10(i) for i in range(2, n + 1))
        print(int(log_sum) + 1)