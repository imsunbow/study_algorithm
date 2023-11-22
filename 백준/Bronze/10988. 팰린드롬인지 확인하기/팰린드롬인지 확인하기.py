#백준 10988

N = input()

if N[::1] == N[::-1]:
    print(1)
else:
    print(0)

