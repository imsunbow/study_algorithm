n, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def matrix_mult(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def matrix_pow(mat, exp):
    size = len(mat)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]    
    while exp:
        if exp % 2 == 1:
            result = matrix_mult(result, mat)
        mat = matrix_mult(mat, mat)
        exp //= 2
    return result

result = matrix_pow(board, b)

for row in result:
    print(' '.join(map(str, row)))