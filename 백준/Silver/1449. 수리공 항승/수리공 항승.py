n, l = map(int, input().split())
leaks = list(map(int, input().split()))

leaks.sort()

cnt = 0
i = 0

while i < n:
    end_len = leaks[i] - 0.5 + l
    cnt += 1
    while i < n and leaks[i] < end_len:
        i += 1
        
print(cnt)