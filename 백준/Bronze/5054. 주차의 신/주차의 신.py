#백준 5054: 주차의 신

T = int(input())

for _ in range(T):
    N = int(input())
    distance = sorted(map(int,input().split()))

    print((distance[-1] - distance[0]) * 2)