from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
def bfs(start, end):
    visited = [False] * (n + 1) 
    dist = [0] * (n + 1)
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        if node == end:
            return dist[node]

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
    
    return -1 

print(bfs(start, end))