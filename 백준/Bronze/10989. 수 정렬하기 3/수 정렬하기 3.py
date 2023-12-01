#백준 10989 수 정렬하기 3

import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] * (10000+1)

for i in range(N):
    numbers[(int(input()))] += 1

for i in range(len(numbers)):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)