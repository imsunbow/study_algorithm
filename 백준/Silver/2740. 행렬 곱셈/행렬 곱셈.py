# 백준 2740: 행렬 곱셈

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
m, k = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(m)]

c = [[0] * k for _ in range(n)]

# calculate matrix using nested loop
for i in range(n):
    for j in range(k):
        for l in range(m):
            c[i][j] += a[i][l] * b[l][j] #calculate

for row in c:
    print(*row)
            