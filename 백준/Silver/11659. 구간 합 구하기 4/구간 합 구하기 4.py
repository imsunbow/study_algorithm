#백준 11659: 구간 합 구하기 4
import sys

n,m = map(int,sys.stdin.readline().split())

prefix_sum = [0]
current_sum = 0

#부분합 구하기
for num in map(int, sys.stdin.readline().split()):
    current_sum += num
    prefix_sum.append(current_sum)

#결과 출력
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    result = prefix_sum[b] - prefix_sum[a - 1]
    print(result)