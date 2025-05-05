#백준 1806: 부분합

n,s = map(int, input().split())

lst = list(map(int, input().split()))

start = 0
end = 0
total = 0

min_length = n + 1

while end < n:
    total += lst[end]
    end += 1

    while total >= s:
        min_length = min(min_length, end - start)
        total -= lst[start]
        start += 1  

if min_length == n + 1:
    print(0)
else:
    print(min_length)
    
    