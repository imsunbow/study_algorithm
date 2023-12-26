#백준 15726: 이칙연산

a,b,c = map(int,input().split())

if a > b > c or b > a > c or a == b > c:
    print(int(a*b/c))
else:
    print(int(a/b*c))
