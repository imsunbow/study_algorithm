#백준 31090: 2023은 무엇이 특별할까?

T = int(input())

for _ in range(T):
    N = int(input())
    K = N % 100

    if (N+1) % K == 0:
        print("Good")
    else:
        print("Bye")