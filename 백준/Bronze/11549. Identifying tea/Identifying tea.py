#백준 11549: 차 식별

cnt = 0

#입력
T = int(input())
a,b,c,d,e = map(int,input().split())

if a == T:
    cnt +=1
if b == T:
    cnt +=1
if c == T:
    cnt +=1
if d == T:
    cnt +=1
if e == T:
    cnt +=1

print(cnt)