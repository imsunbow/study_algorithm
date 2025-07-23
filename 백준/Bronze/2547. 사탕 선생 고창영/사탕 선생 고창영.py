# 백준 2547 : 사탕 선생 고창영

t = int(input())

for _ in range(t):
    emp = input("")
    n = int(input())
    candy_lst = [int(input()) for _ in range(n)]
    print('YES' if sum(candy_lst) % n == 0 else 'NO')   