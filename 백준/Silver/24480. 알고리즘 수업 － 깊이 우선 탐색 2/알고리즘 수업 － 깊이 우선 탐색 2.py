import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5) # set recursion limit cause deep recursion may occur

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m): # general way to build an undirected graph -> adjacency list
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n + 1):
    graph[i].sort(reverse=True)  # sort by descending order

visited = [0] * (n + 1)
cnt = [1]

# if visited[neighbor] == 0 -> dfs(neighbor)
def dfs(node):
    visited[node] = cnt[0]
    cnt[0] += 1
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            dfs(neighbor)

dfs(r)
print('\n'.join(map(str, visited[1:]))) 