# 백준 2965: 캥거루 세 마리

a, b, c = map(int,input().split())
print(max(b-a,c-b) - 1) # No need for abs cause a < b < c is guaranteed