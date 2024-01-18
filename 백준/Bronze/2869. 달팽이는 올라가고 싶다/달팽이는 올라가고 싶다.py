import math
A,B,V= map(int,input().split())
    
N= math.ceil((V-B)/(A-B))
print(N)