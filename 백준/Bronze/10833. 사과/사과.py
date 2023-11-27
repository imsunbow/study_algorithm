#백준 10833

N = int(input())
remain = 0

for _ in range(N):
    a,b = map(int,input().split())
    remain += b % a

print(remain)
