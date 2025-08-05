a, b = map(int, input().split())
k, x = map(int, input().split())

cnt = 0

for i in range(k - x, k + x + 1):
    if a <= i <= b:
        cnt += 1
                          
print(cnt if cnt > 0 else "IMPOSSIBLE")