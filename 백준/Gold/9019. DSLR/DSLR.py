import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    visited = [False] * 10000
    queue = deque()
    queue.append((a, ""))
    visited[a] = True

    while queue:
        num, ops = queue.popleft()
        if num == b:
            return ops

        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            queue.append((d, ops + 'D'))

        s = 9999 if num == 0 else num - 1
        if not visited[s]:
            visited[s] = True
            queue.append((s, ops + 'S'))

        l = (num % 1000) * 10 + (num // 1000)
        if not visited[l]:
            visited[l] = True
            queue.append((l, ops + 'L'))

        r = (num % 10) * 1000 + (num // 10)
        if not visited[r]:
            visited[r] = True
            queue.append((r, ops + 'R'))

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))
