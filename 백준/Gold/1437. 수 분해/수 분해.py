import sys

input = sys.stdin.readline

n = int(input())

MOD = 10007

if n == 0:
    print(0)
else:
    ans = 1
    while n > 4:
        ans = (ans * 3) % MOD
        n -= 3
    print((ans * n) % MOD)