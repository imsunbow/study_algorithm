#백준 1564: 팩토리얼5

import sys
input = sys.stdin.readline

n = int(input())
res = 1

for i in range(2, n+1):
    res *= i

    while res % 10 == 0:
        res //= 10

    res %= 100000000000000

while res % 10 == 0:
    res //= 10

print(str(res)[-5:])

