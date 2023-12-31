#백준 1002: 터렛
import math

T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    else:
        if r1+r2 == dis or abs(r2-r1) == dis:
            print(1)
        elif r1+r2 > dis and dis > abs(r1-r2):
            print(2)
        else:
            print(0)
