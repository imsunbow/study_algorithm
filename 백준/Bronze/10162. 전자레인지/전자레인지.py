#백준 10162

N = int(input())

def timer(N):
    A = N // 300
    N %= 300
    B = N // 60
    N %= 60
    C = N // 10
    N %= 10

    if N !=0:
        return -1

    return f"{A} {B} {C}"

print(timer(N))



