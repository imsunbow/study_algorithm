import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, input().split())    
    if op == 0:
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
    else: # op == 1 (same union)
        print("YES" if find(a) == find(b) else "NO")