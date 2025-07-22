import sys
input = sys.stdin.readline

a, b = map(int,input().split())

res = [str(a//b), '.']
a = (a % b) * 10 

for _ in range(2001):
    res.append(str(a // b))
    a = (a % b) * 10
    
print(''.join(res))