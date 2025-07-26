import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x: x[1])

lec_room = []
cnt = 0

# main idea : leave lecture room if lecture ends before another lecture starts (using heap)

for i in lst:
    while lec_room and lec_room[0] <= i[1]:
        heapq.heappop(lec_room) # leave lecture room
    heapq.heappush(lec_room, i[2]) # add end time to lecture room
    cnt = max(cnt, len(lec_room))

print(cnt)