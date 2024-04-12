#백준 10026: 적록색약

import sys
sys.setrecursionlimit(10 ** 4)

# 함수 생성
def dfs(x, y, c):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                if c == graph[nx][ny]:
                    dfs(nx, ny, c)

# 입력
n = int(sys.stdin.readline())

# 그래프 생성, 탐색 여부 초기화(default= false)
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 일반인
cnt1 = 0

# 방문하지 않은 노드 방문 후 cnt 증가
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            cnt1 += 1

# 적록색약 세팅
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

# 적록색약
cnt2 = 0
visited = [[False] * n for _ in range(n)]

# 적록색약 카운트
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            cnt2 += 1

# 출력
print(cnt1, cnt2)
