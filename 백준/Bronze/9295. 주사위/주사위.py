#백준 9295

T = int(input())
n = 0

for _ in range(T):
    a,b = map(int,input().split())
    n += 1

    print("Case {}: {}".format(n,a+b))