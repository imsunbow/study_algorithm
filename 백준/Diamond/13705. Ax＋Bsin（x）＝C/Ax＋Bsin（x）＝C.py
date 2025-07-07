# 백준 13705: Ax + Bsinx = C

import math
import decimal
import sys

input = sys.stdin.readline

# set decimal precision
decimal.getcontext().prec = 100
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

# input
a, b, c = map(decimal.Decimal, input().split())

# set pi with high precision (reason why we use decimal is to avoid floating point precision issues)
pi = decimal.Decimal("3.1415926535897932384626433832795028841")

# precision for convergence
precision = decimal.Decimal("0." + ("0" * 50) + "1")

# taylor series expansion for sin(x)
def sin_precision(x: decimal.Decimal) -> decimal.Decimal:
    x = x % (2 * pi)
    term = x
    result = x
    n = 1
    while abs(term) >= precision:
        term *= -x * x / ((2 * n) * (2 * n + 1)) 
        result += term
        n += 1
    return result

# define f(x)
def f(x: decimal.Decimal) -> decimal.Decimal:
    return a * x + b * sin_precision(x)

# BS
l = decimal.Decimal("0")
r = decimal.Decimal("100000")

while r - l > decimal.Decimal("1e-30"):
    mid = (l + r) / 2
    if f(mid) < c:
        l = mid
    else:
        r = mid

ans = (l + r) / 2
print(ans.quantize(decimal.Decimal("0.000001")))
