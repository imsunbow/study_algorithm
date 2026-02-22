import sys
input = sys.stdin.readline

a, b = 0, 1

k = int(input())

for _ in range(1, k):
    a, b = b, a+b
    
print(a, b)