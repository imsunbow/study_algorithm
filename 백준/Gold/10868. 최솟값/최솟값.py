#백준 3273: 두 수의 합

import sys

#입력
n,m = map(int, sys.stdin.readline().split())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

#누적 최솟값 리스트 생성
min_values = [float('inf')] * (4 * n)
def init_min(segment_start, segment_end, node):
    if segment_start == segment_end:
        min_values[node] = numbers[segment_start - 1]
        return min_values[node]

    mid = (segment_start + segment_end) // 2
    min_values[node] = min(init_min(segment_start, mid, 2 * node), init_min(mid + 1, segment_end, 2 * node + 1))
    return min_values[node]

init_min(1, n, 1)

#구간 최솟값 조회
def query_min(left, right, segment_start, segment_end, node):
    if right < segment_start or left > segment_end:
        return float('inf')
    if left <= segment_start and right >= segment_end:
        return min_values[node]

    mid = (segment_start + segment_end) // 2
    return min(query_min(left, right, segment_start, mid, 2 * node), query_min(left, right, mid + 1, segment_end, 2 * node + 1))

#출력
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    result = query_min(a, b, 1, n, 1)
    print(result)
