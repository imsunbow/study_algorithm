# 백준 10250 : ACM 호텔

T = int(input())

for _ in range(T):
    H,W,N = map(int,input().split())
    q,r = divmod(N-1,H)
    print((r+1) * 100+q+1)