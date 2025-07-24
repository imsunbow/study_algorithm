r,k,m=map(int, input().split())
halvings=min(m//k,r.bit_length()) 
print(r>>halvings)