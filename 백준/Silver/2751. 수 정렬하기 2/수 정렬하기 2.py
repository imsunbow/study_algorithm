# 백준 2751

N = int(input())

num = [0] * N

for i in range(N):
    num[i] = int(input())
num.sort()

for j in num:
    print(j)


