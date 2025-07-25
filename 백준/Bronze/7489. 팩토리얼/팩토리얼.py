from math import factorial

t = int(input())

for _ in range(t):
    n = str(factorial(int(input())))
    for digit in reversed(n):
        if digit != '0':
            print(digit)
            break