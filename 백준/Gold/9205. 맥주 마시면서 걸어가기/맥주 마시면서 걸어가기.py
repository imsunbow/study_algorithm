from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n+2)] 
    visited = [False] * (n+2)
    
    q = deque([0]) 
    visited[0] = True
    found = False
    
    while q:
        now = q.popleft()
        if now == n+1:
            found = True
            break
        for i in range(n+2):
            if not visited[i]:
                dist = abs(points[now][0] - points[i][0]) + abs(points[now][1] - points[i][1])
                if dist <= 1000:
                    visited[i] = True
                    q.append(i)
                    
    print("happy" if found else "sad")