import sys
input = sys.stdin.readline

s = input()
q = int(input())

for _ in range(q):
    alpha, l, r = input().split()
    l = int(l)
    r = int(r)
    
    count = 0    
    for i in range(l, r + 1):
        if s[i] == alpha:
            count += 1
    print(count)