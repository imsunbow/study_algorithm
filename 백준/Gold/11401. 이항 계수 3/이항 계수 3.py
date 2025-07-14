#백준 11401 : 이항계수 3

# 시간초과코드 (runtime error)
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# N,K = map(int,input().split())
# print((factorial(N) // (factorial(K) * factorial(N-K)) % 1000000007)) 


# sol > 큰 팩토리얼은 미리 fact에 저장하여 연산
MOD = 10 ** 9 + 7 
MAX = 4000001

fact = [1] * MAX

for i in range(1,MAX):
    fact[i] = fact[i-1] * i % MOD

def modinv(x):
    return pow(x, MOD -2, MOD)

n,k = map(int,input().split())

res = fact[n] * modinv(fact[k]) % MOD
res = res * modinv(fact[n-k]) % MOD

print(res)