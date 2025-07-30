import sys,heapq

input = sys.stdin.readline
lst = [int(input()) for _ in range(int(input()))]
lst.sort()

cnt = 0

while len(lst) > 1:
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    cnt += a + b
    heapq.heappush(lst, a + b)
    
print(cnt)