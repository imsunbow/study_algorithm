t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    cnt = 0
    
    # sol : brute force 
    for x in range(1, a+1):
        for y in range(1, b+1):
            for z in range(1, c+1):
                if (x % y) == (y % z) == (z % x):
                    cnt += 1
                    
    print(cnt)