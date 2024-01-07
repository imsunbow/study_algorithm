#백준 1010: 다리 놓기

def factorial(N): #팩토리얼 정의
    if N > 1:
        return(N * factorial(N-1))
    else:
        return 1

T = int(input())

for _ in range(T): #nCr 조합 추출
    N,M = list(map(int,input().split()))
    print(factorial(M) // (factorial(M-N) * factorial(N)))



