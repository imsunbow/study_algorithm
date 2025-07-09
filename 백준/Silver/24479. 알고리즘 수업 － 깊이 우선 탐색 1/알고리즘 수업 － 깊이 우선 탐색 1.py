
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(start):
    stack = [start]
    visited = [False] * (n + 1)
    order = [0] * (n + 1)
    cnt = 1

    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        order[node] = cnt
        cnt += 1
        # Push neighbors in reverse order for correct ascending DFS
        for neighbor in reversed(graph[node]):
            if not visited[neighbor]:
                stack.append(neighbor)
    return order

result = dfs(r)
print('\n'.join(map(str, result[1:])))