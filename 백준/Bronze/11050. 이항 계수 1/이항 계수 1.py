#백준 11050 : 이항계수 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

N,K = map(int,input().split())
print(factorial(N) // (factorial(K) * factorial(N-K)))