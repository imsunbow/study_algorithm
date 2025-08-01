import sys

input = sys.stdin.readline

def xor(n):    
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(xor(B) ^ xor(A - 1))