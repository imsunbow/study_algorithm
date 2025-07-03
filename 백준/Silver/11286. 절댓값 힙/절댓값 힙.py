#백준 11286: 절댓값 힙

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    input_value = int(input())
    if input_value == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (abs(input_value) , input_value))

