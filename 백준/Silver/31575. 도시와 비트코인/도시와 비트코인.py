from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

start = (0, 0)
directions = [(0, 1), (1, 0)] 

visited = [[False] * n for _ in range(m)]
visited[0][0] = True

q = deque([start])
check_way = False # set default as False

while q:
    y, x = q.popleft()

    if y == m - 1 and x == n - 1:
        check_way = True
        break

    for dy, dx in directions:
        ny, nx = y + dy, x + dx

        if 0 <= ny < m and 0 <= nx < n:
            if not visited[ny][nx] and board[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((ny, nx))

print("Yes" if check_way else "No")