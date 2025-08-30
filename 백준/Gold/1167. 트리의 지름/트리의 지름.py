
import sys
from collections import deque

input = sys.stdin.readline

num_vertices = int(input())
tree = [[] for _ in range(num_vertices + 1)]

for _ in range(num_vertices):
    data = list(map(int, input().split()))
    node = data[0]
    idx = 1
    while data[idx] != -1:
        neighbor = data[idx]
        distance = data[idx + 1]
        tree[node].append((neighbor, distance))
        idx += 2

def bfs(start_node):
    visited = [-1] * (num_vertices + 1)
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 0
    farthest_distance = 0
    farthest_node = start_node

    while queue:
        current = queue.popleft()
        for neighbor, weight in tree[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + weight
                queue.append(neighbor)
                if visited[neighbor] > farthest_distance:
                    farthest_distance = visited[neighbor]
                    farthest_node = neighbor
    return farthest_node, farthest_distance


farthest_from_start, farthest_distance = bfs(1)

farthest_distance, diameter = bfs(farthest_from_start)
print(diameter)