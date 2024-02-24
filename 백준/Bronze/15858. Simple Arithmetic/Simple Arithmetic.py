#백준 15858: Simple Arithmatic

from decimal import Decimal

try:
    a, b, c = map(int, input().split())
    result = Decimal(a) * Decimal(b) / Decimal(c)
    print(result)
except ZeroDivisionError:
    print()
except ValueError:
    print()

