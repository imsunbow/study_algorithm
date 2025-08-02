n = int(input())

lst = [int(input()) for _ in range(n)]

res = 0
for i in range(n-1):
    res += (lst[i+1] - lst[i]) ** 2

print(res)