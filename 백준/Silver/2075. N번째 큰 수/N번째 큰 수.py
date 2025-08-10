import heapq
import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

heap = []
for col in range(n):
    heapq.heappush(heap, (-board[n-1][col], n-1, col))
    
visited = set()

for _ in range(n):
    value, row, col = heapq.heappop(heap)
    result = -value
    
    # if not visited
    if row > 0 and (row-1, col) not in visited:
        heapq.heappush(heap, (-board[row-1][col], row-1, col)) # push minimum heap
        visited.add((row-1, col))
        
print(result)