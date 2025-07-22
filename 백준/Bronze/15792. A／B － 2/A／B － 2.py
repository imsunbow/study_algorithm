import sys
from decimal import Decimal, getcontext

getcontext().prec = 101 # precize should be over 100 

input = sys.stdin.readline

a,b = map(int,input().split())
res =  Decimal(a)/ Decimal(b)

print(f"{res:.100f}")