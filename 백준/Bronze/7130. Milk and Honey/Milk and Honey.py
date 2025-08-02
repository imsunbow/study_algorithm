m, h = map(int, input().split())
n = int(input())

res = 0

for _ in range(n):
    c, b = map(int, input().split())
    cow = c * m
    bee = b * h
    res += max(cow, bee)

print(res)