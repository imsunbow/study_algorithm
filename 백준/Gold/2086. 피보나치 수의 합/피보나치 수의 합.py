# 백준 2086 : 피보나치 수의 합

import sys
input = sys.stdin.readline
MOD = 1000000000

def mul(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def power(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return matrix
    half = power(matrix, n // 2)
    if n % 2 == 0:
        return mul(half, half)
    else:
        return mul(mul(half, half), matrix)

def fib(n):
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    return power(base, n - 1)[0][0]

a, b = map(int, input().split())

sum_fib = (fib(b + 2) - fib(a + 1)) % MOD
print(sum_fib)