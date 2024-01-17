#백준 10845: 큐

from sys import stdin

n = int(stdin.readline())
Que = []

for i in range(n):
    A = stdin.readline().split()

    if A[0] == 'push': #push
        Que.append(A[1])

    elif A[0] == 'pop': #pop
        if Que:
            print(Que.pop(0))
        else:
            print(-1)

    elif A[0] == 'size': #size
        print(len(Que))

    elif A[0] == 'empty': #empty
        if len(Que) == 0:
            print(1)
        else:
            print(0)

    elif A[0] == 'front': #front
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[0])

    elif A[0] == 'back': #back
        if len(Que) == 0:
            print(-1)
        else:
            print(Que[-1])



