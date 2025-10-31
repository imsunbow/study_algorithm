import sys

input = sys.stdin.readline

def dfs():

    if len(str) == m:
        print(*str)

    for i in range(1, n + 1):
        if i in str:
            continue
        str.append(i)
        dfs()
        str.pop()


n, m = map(int, input().split())

str = []

dfs()
