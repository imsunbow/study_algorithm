time = float('inf')

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        time = min(time, b)

print(-1 if time == float('inf') else time)