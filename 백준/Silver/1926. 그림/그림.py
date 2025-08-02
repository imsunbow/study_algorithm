# 백준 1926 : 그림

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    dq = deque([(x, y)])
    visited[x][y] = True
    area = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                    area += 1

    return area


cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            cnt += 1
            max_area = max(max_area, bfs(i, j))

print(cnt)
print(max_area)
