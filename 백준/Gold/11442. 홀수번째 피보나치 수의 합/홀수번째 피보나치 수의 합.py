MOD = 10**9 + 7

def mat_mul(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def mat_pow(mat, n):
    result = [[1, 0], [0, 1]]  
    while n > 0:
        if n % 2 == 1:
            result = mat_mul(result, mat)
        mat = mat_mul(mat, mat)
        n //= 2
    return result

def fibonacci(n):
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    return mat_pow(base, n-1)[0][0]

n = int(input())

if n % 2 == 0:
    print(fibonacci(n) % MOD)
else:
    print((fibonacci(n + 1) - 1 + MOD) % MOD + 1)  