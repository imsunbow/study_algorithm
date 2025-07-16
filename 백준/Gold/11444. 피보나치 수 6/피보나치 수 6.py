# 백준 11444: 피보나치 수 6 (핵심 알고리즘 : 분할정복 with 거듭제곱법)

import sys
input = sys.stdin.readline

MOD = 1000000007

def mul(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def power(matrix, n):
    if n == 0:
        return [[1, 0],[0, 1]]
    elif n == 1:
        return matrix
    half = power(matrix, n//2) # devide and conquer by using exponential
    if n % 2 == 0:
        return mul(half, half)
    else:
        return mul(mul(half, half), matrix)
    
# input/ output    
n = int(input())
if n == 0:
    print(0)
else:
    base = [[1, 1], [1, 0]]
    result = power(base, n - 1)
    print(result[0][0])


# 백준 11444: 피보나치 수 6  (실패코드. 사유 : 메모리 초과)

# import sys
# input = sys.stdin.readline

# n = int(input())

# fibo = [0,1]
# p = (1000000007//10)*15

# for i in range(2,p):
#     fibo.append(fibo[i-1]+fibo[i-2])
#     fibo[i] %= 1000000007

# print(fibo[n%p])