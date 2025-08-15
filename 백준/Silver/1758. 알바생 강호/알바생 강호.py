n = int(input())
tips = [int(input()) for _ in range(n)]

tips.sort(reverse=True)

res = 0

for i in range(n):
    temp = tips[i] - i
    if temp > 0:
        res += temp
print(res)