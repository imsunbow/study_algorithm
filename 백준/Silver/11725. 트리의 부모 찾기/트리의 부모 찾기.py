import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())

parent = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(node, par):
    parent[node] = par
    for child in graph[node]:
        if child != par:
            dfs(child, node)

dfs(1, 0)
for i in range(2, n + 1):
    print(parent[i])