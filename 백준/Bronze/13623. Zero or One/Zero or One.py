#백준 13623: zero or one

a,b,c = map(int,input().split())

if a == b == c:
    print("*")
elif a == b and a != c:
    print("C")
elif b == c and b != a:
    print("A")
elif a == c and a != b:
    print("B")


