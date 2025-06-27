import sys
from collections import deque

input = sys.stdin.readline
a,b = map(int, input().split())
limit = 10**5 + 1

time = [0] * limit

def bfs(start, end):
    q = deque()
    if start == 0:
        q.append(1)
    else:
        q.append(start)

    while q:
        start = q.popleft()
        if end == start:
            return time[start]
        
        for next in (start - 1, start + 1, start * 2):
            if 0 <= next < limit and time[next] == 0:
                if next == 2* start:
                    time[next] = time[start]
                    q.appendleft(next)
                else:
                    time[next] = time[start] + 1
                    q.append(next)

                
# output

if a == 0:
    if b== 0:
        print(0)
    else:
        print(bfs(a,b)+1)
else:
    print(bfs(a,b))