# 백준 1238 : 파티

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# Read inputs
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# Build the directed graph
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# Dijkstra algorithm: returns shortest distances from 'start' to all nodes
def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (cost, node)

    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node] < cost:
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return dist

# Distance from all nodes to X
to_x = [0] * (n + 1)
for i in range(1, n + 1):
    to_x[i] = dijkstra(i)[x]

# Distance from X to all nodes (only once)
from_x = dijkstra(x)

# Calculate round-trip times
max_time = 0
for i in range(1, n + 1):
    total_time = to_x[i] + from_x[i]
    max_time = max(max_time, total_time)

print(max_time)
