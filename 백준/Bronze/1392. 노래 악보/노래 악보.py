n, q = map(int, input().split())

time_lst = list(int(input()) for _ in range(n))

for _ in range(q):
    t = int(input())
    for i in range(n):
        if t < sum(time_lst[:i+1]):
            print(i+1)
            break