from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    arr_str = input().strip()
    
    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr_str[1:-1].split(',')))

    # initialize
    reverse = False
    error = False

    for cmd in p:
        if cmd == 'R' :
            reverse = not reverse
        elif cmd == 'D':
            if not arr:
                error = True
                break
            
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    # print
    if error:
        print("error")
    else:
        if reverse:
            print("[" + ",".join(map(str, reversed(arr))) + "]")
        else:
            print("[" + ",".join(map(str, arr)) + "]")