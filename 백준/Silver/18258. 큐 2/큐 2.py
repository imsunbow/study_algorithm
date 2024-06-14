#백준 18258: 큐2

import sys
from sys import stdin
from collections import deque

queue = deque()

#함수 생성
def push(x):
    queue.append(x)

def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.popleft())

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])


n = int(stdin.readline())
for i in range(n):
    word = stdin.readline().split()
    if word[0] == 'push':
        push(int(word[1]))
    elif word[0] == 'pop':
        pop()
    elif word[0] == 'size':
        size()
    elif word[0] == 'empty':
        empty()
    elif word[0] == 'front':
        front()
    elif word[0] == 'back':
        back()





