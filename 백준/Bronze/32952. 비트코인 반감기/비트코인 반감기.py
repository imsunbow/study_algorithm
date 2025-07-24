# 백준 32952 : 비트코인 반감기

r, k, m = map(int,input().split())

i = m // k

while i > 0 and r > 0:
    r >>= 1 # bit moving
    i -= 1
    
print(r)