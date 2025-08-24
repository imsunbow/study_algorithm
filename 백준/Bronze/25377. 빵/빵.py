time = []

n = int(input())

for _ in range(n):
    a, b  = map(int, input().split())
    if a < b:
        time.append(b)

time.sort()

print(time[0] if len(time) > 0 else -1)