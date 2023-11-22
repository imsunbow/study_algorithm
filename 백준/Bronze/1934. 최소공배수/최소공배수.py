import math
import sys

num = int(input())
for i in range(0, num):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))
