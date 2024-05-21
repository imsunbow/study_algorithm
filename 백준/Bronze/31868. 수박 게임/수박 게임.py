#백준 31868: 수박 게임

n, k = map(int, input().split())

for _ in range(n-1):
    k//=2

print(k)
