#백준 1012: 유기농 배추

import sys
sys.setrecursionlimit(10**4)

def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #배추이면 > -1로 표시
        if (0 <= nx < m) and (0 <= ny < n) and box[ny][nx] == 1:
            box[ny][nx] = -1
            dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    box = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x,y = map(int,input().split())
        box[y][x] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if box[j][i] == 1:
                dfs(i,j)
                cnt += 1

    print(cnt)





