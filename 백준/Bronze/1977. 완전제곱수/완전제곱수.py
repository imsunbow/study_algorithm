#백준 1977
import math

M = int(input())
N = int(input())

list = []

for i in range(M,N+1):
    if int(math.sqrt(i)) ** 2 == i:
        list.append(i)

if list:
    print(sum(list))
    print(min(list))
else:
    print(-1)





