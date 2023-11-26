import math
import sys

a, b = map(int, sys.stdin.readline().split())
print('1' * math.gcd(a, b))