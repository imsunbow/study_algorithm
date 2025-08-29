import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    m = min(a, b, c)
    print(m)