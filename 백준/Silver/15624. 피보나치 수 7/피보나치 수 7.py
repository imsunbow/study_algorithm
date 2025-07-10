# 백준 15624: 피보나치 수 7

import sys
input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, (a + b) % 1000000007
        return b

n = int(input())
print(fibonacci(n)) 