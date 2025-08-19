import random
import sys
from math import gcd

sys.setrecursionlimit(10 ** 5)

# this code below cannot be solved by Sieve of Eratosthenes
# cause it needs to check for non-trivial factors
# so we've got to use a different approach, Pollard's Rho and Miller-Rabin algortithm instead

# Miller-Rabin algorithm : algorithm used to see whether or not n is prime_number 
def is_prime(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11]:
        if n % p == 0:
            return n == p # True if n == p else False

    d = n - 1
    s = 0
    
    while d % 2 == 0:
        d //= 2
        s += 1
        
    for a in [2, 3, 5, 7, 11]:
        if a >= n:
            continue
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        c = random.randrange(1, n)
        f = lambda x: (pow(x, 2, n) + c) % n
        x, y, d = 2, 2, 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
        if d != n:
            return d

# Pollard's Rho algorithm : algorithm used to find a non-trivial factor of n
def factor(n):
    res = []
    def _factor(n):
        if n == 1:
            return
        if is_prime(n):
            res.append(n)
            return
        d = pollard_rho(n)
        _factor(d)
        _factor(n // d)
    _factor(n)
    return sorted(res)

n = int(input())

for res in factor(n):
    print(res)