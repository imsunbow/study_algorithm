k, w, m = map(int, input().split())

need = w - k

if need <= 0:
    print(0)
else:
    print((need + m - 1) // m)  