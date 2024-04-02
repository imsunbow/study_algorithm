#백준 14425: 문자열 집합

import sys

n,m = map(int,sys.stdin.readline().split())
cnt = 0

lst1 = set()
cnt = 0

for _ in range(n):
    lst1.add(input())

for _ in range(m):
    if input() in lst1:
        cnt += 1

print(cnt)