import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
	u, v, w = map(int, input().split())
	graph[u].append((v, w))

start, end = map(int, input().split())

dist = [float('inf')] * (n+1)

dist[start] = 0 # from city
q = [(0, start)] # start

# find shortest path using Dijkstra's algorithm
while q:
	cost, now = heapq.heappop(q)
	if dist[now] < cost:
		continue
	for to, w in graph[now]:    
		if dist[to] > cost + w:
			dist[to] = cost + w
			heapq.heappush(q, (dist[to], to))
   
print(dist[end])