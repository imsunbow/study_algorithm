#백준 6504: 킬로미터를 마일로

#초기화
fib = [0] * 21
fib[0] = 1
fib[1] = 2

for i in range(2, 21):
    fib[i] = fib[i - 1] + fib[i - 2]

T = int(input())

while T > 0:
    ans = 0
    x = int(input())
    i = 20
    while i > 0:
        if x >= fib[i]:
            x -= fib[i]
            ans += fib[i - 1]
        i -= 1

    print(ans)
    T -= 1
