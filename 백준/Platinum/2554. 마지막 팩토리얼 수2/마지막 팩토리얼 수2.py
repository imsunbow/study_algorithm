def power(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result

def last_nonzero_digit(n):
    if n < 5:
        return [1, 1, 2, 6, 4][n]
    
    # mathmetical recursion
    q = n // 5
    r = n % 5
    return (last_nonzero_digit(q) * power(2, q, 10) * [1, 1, 2, 6, 4][r]) % 10

# input: up to 100 digits as a string
import sys
input = sys.stdin.readline

n_str = input().strip()

# Convert the string input to an integer
n = int(n_str)
print(last_nonzero_digit(n))