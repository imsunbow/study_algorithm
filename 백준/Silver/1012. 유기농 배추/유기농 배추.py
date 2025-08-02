import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def dfs(row, col):
    dx = [-1, 1, 0, 0]  
    dy = [0, 0, -1, 1]  

    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]

        if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
            field[nx][ny] = -1
            dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split()) 
    field = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
