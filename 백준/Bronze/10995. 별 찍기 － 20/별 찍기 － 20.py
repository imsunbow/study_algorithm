# 백준 10995

N = int(input())

for i in range(1,N+1):
    if i%2 ==1:
        print('* ' * N)
    elif i%2 ==0:
        print(' *' * N)

