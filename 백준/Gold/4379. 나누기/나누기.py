import sys,math
input = sys.stdin.readline
while True:
    l = input().split()
    if not l:break
    a, b, c = map(int, l)
    s = f'({a}^{b}-1)/({a}^{c}-1)'
    if a != 1 and b % c == 0:
        if round((b - c) * math.log10(a), 10) < 100:
            p = b // c
            t = 0
            for i in range(p):
                t += a ** (c * i)
            if len(str(t)) < 100:
                print(s, t)
                continue
    print(s, 'is not an integer with less than 100 digits.')