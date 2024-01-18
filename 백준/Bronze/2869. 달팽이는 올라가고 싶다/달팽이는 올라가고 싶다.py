#백준 2869: 달팽이는 올라가고 싶다

A,B,V = map(int,input().split())

T = (V-B) // (A-B) #계산식

if (V-B) % (A-B) == 0:
    print(int(T))
else:
    print(int(T)+1)