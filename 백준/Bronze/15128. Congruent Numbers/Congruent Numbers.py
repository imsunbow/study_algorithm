import math

p1, q1, p2, q2 = map(int, input().split())

numerator = p1 * p2
denominator = q1 * q2 * 2 

gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

print(1 if denominator == 1 else 0)