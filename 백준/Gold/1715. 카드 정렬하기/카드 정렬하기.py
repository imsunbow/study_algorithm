import sys
import heapq

input = sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    size = int(input())
    lst.append(size)
    
lst.sort()

cnt = 0

while len(lst) > 1:
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    cnt += a + b
    heapq.heappush(lst, a + b)
    
print(cnt)