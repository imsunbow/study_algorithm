# 백준 24482: 알고리즘 수업 - 깊이 우선 탐색 4

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for adj in graph:
    adj.sort(reverse= True)

def dfs(node, depth):
    visited[node] = depth
    for neighbor in graph[node]:
        if visited[neighbor] == -1:
            dfs(neighbor, depth + 1)

dfs(r, 0)

for d in visited[1:]:
    print(d)
