#백준 10797

N = int(input())
a,b,c,d,e = map(int,input().split())
count = 0

if N == a:
    count += 1
if N == b:
    count += 1
if N == c:
    count += 1
if N == d:
    count += 1
if N == e:
    count += 1

print(count)