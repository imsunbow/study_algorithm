from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for adj in graph: # sort adjacency list
    adj.sort()
    
visited = [0] * (n + 1)
queue = deque([r])  # add start peak to queue
visited[r] = 1 # mark start point
order = 1 # visiting sequence

while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if not visited[neighbor]: # if not visited neighbor -> order + 1
            order += 1
            visited[neighbor] = order
            queue.append(neighbor)

for i in range(1, n + 1):
    print(visited[i])  # print visited order