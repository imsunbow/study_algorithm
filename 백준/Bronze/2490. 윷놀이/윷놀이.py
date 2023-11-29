#백준 2490

for _ in range(3):
    a,b,c,d = map(int,input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        print("D")
    elif a == 1 and b == 1 and c == 1 and d == 1:
        print("E")
    elif a == 0 and b == 1 and c == 1 and d == 1:
        print("A")
    elif a == 1 and b == 0 and c == 1 and d == 1:
        print("A")
    elif a == 1 and b == 1 and c == 0 and d == 1:
        print("A")
    elif a == 1 and b == 1 and c == 1 and d == 0:
        print("A")
    elif a == 0 and b == 0 and c == 1 and d == 1:
        print("B")
    elif a == 0 and b == 1 and c == 0 and d == 1:
        print("B")
    elif a == 0 and b == 1 and c == 1 and d == 0:
        print("B")
    elif a == 1 and b == 0 and c == 0 and d == 1:
        print("B")
    elif a == 1 and b == 0 and c == 1 and d == 0:
        print("B")
    elif a == 1 and b == 1 and c == 0 and d == 0:
        print("B")
    elif a == 0 and b == 0 and c == 0 and d == 1:
        print("C")
    elif a == 0 and b == 0 and c == 1 and d == 0:
        print("C")
    elif a == 0 and b == 1 and c == 0 and d == 0:
        print("C")
    elif a == 1 and b == 0 and c == 0 and d == 0:
        print("C")


