import sys
import math
input = sys.stdin.readline

while True:
    line = input().split()
    if not line:
        break
    a, b, c = map(int, line)
    expr = f'({a}^{b}-1)/({a}^{c}-1)'
    
    # validation check
    if a != 1 and b % c == 0:
        # estimate the length of the input
        if round((b - c) * math.log10(a), 10) < 100:
            p = b // c
            total = 0
            # sum of by using for statement
            for i in range(p):
                total += a ** (c * i)
            # check the length
            if len(str(total)) < 100:
                print(expr, total)
                continue

    print(expr, 'is not an integer with less than 100 digits.')