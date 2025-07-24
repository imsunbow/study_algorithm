import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
times = list(map(int, input().split()))

ab = a + b
cd = c + d

for time in times:
    dog = 0
    mod_ab = time % ab
    mod_cd = time % cd
    
    if 0 < mod_ab <= a:
        dog += 1
    if 0 < mod_cd <= c:
        dog += 1
    
    print(dog)