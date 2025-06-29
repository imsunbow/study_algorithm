# 백준 2553 : 마지막 팩토리얼 수

from math import factorial

n = str(factorial(int(input())))

for degit in reversed(n):
    if degit != '0':
        print(degit)
        break