#백준 27294: 몇개고?

t,s = map(int,input().split())

if t <= 16 and t >= 12:
    if s == 0:
        print("320")
    else:
        print("280")
else:
    print("280")
