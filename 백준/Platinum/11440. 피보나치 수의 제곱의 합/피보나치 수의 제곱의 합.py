MOD = 10**9 + 7

def mat_mul(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def mat_pow(mat, power):
    result = [[1, 0], [0, 1]]  
    base = mat
    while power > 0:
        if power & 1:
            result = mat_mul(result, base)
        base = mat_mul(base, base)
        power >>= 1 # bit shift
    return result

def fib(n):
    if n == 0:
        return 0
    base_mat = [[1, 1], [1, 0]]
    res_mat = mat_pow(base_mat, n - 1)
    return res_mat[0][0]

n = int(input())

fn = fib(n)
fn_plus_1 = fib(n + 1)
answer = (fn * fn_plus_1) % MOD

print(answer)