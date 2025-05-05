
#백준 1051: 숫자 정사각형

n,m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
max_square = 1

for i in range(n):
    for j in range(m):
        for k in range(1, min(n-i, m-j)):
            if arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]:
                max_square = max(max_square, (k+1)**2)
print(max_square)   