# 백준 1240: 노드사이의 거리

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# read edges
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # add edge from a to b with weight c
    graph[b].append((a, c)) # add edge from b to a with weight c

# define bfs
def bfs(start, end):
    visited = [0] * (n+1)
    q = deque()
    q.append((start, 0))  # (current node, current distance
    visited[start] = 1

    while q: # while there are nodeds in the queue
        current, distance = q.popleft() 
        if current == end:
            return distance
        
        # iterate through all adjacent nodes
        for next_node, weight in graph[current]:
            if not visited[next_node]: # if not visited yet
                visited[next_node] = 1 # False -> True (visited)
                q.append((next_node, distance + weight)) # add next node to queue 

for _ in range(m):
    u,v = map(int,input().split())
    print(bfs(u,v))