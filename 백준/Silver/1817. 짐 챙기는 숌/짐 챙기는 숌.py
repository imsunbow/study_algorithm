import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cnt = 0
lst = list(map(int, input().split()))
    
if n == 0:
    print(0)
    sys.exit()
    
cur = 0

for i in lst:
    if cur + i > m:
        cnt += 1
        cur = 0
    cur += i
    
if cur > 0:
    cnt += 1
    
print(cnt)