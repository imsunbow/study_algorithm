#백준 2765: 자전거 속도
from math import pi

cnt = 1

while True:
    diameter, rnd, time = map(float,input().split())
    if rnd == 0:
        break
    dis = diameter/63360 * pi * rnd
    mph = dis/time * 3600
    print(f"Trip #{cnt}: {dis:.2f} {mph:.2f}")
    cnt += 1