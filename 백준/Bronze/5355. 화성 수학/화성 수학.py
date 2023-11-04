t = int(input())

for i in range(t):
    m = list(map(str,input().split()))
    e = float(m[0])

    for i in range(1, len(m)):
        if m[i] == '@':
            e *= 3
        if m[i] == '%':
            e += 5
        if m[i] == '#':
            e -= 7

    print('{:.2f}'.format(e))
