t = int(input())

def max(t):
    N = 1
    while N * (N + 1) // 2 <= t:
        N += 1
    return N - 1

max = max(t)
print(max)