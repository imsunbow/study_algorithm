import sys
from collections import deque

input = sys.stdin.readline

def dfs(node, visited):
    visited[node] = True
    dfs_lst.append(node)
    
    for next_node in adj_node[node]:
        if not visited[next_node]:
            dfs(next_node, visited)
                        
def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    bfs_lst.append(start)
    
    while queue:
        current = queue.popleft()
        
        for next_node in adj_node[current]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                bfs_lst.append(next_node)
    
n, m, v = map(int, input().split())

adj_node = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    adj_node[s].append(e)
    adj_node[e].append(s)
    
for i in range(1, n + 1):
    adj_node[i].sort()
        
dfs_lst = []
bfs_lst = []

visited_dfs = [False] * (n + 1)
dfs(v, visited_dfs)

visited_bfs = [False] * (n + 1)
bfs(v, visited_bfs)

print(*dfs_lst)
print(*bfs_lst)