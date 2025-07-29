import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)

max_load = 0

for i in range(n):
    load = ropes[i] * (i + 1) # weight = rope[i] * (i + 1)
    if load > max_load:
        max_load = load

print(max_load)