import sys

input = sys.stdin.readline

MAX_NUMBER = 318137 # 3000 -> 318137 

is_not_prime = [False] * (MAX_NUMBER + 1) # reset
is_not_prime[1] = True

for i in range(2, int(MAX_NUMBER**0.5) + 1):
    if not is_not_prime[i]:
        for j in range(i * i, MAX_NUMBER + 1, i):
            is_not_prime[j] = True

primes = []
cnt = 0

for i in range(2, MAX_NUMBER + 1):
    if not is_not_prime[i]:
        cnt += 1
        if not is_not_prime[cnt]:
            primes.append(i)

t = int(input())

for _ in range(t):
    n = int(input())
    print(primes[n - 1])
