n=int(input());s=1
while n:s*=[1,1,2,6,4][n%5]*2**((n:=n//5)%4)
print(s%10)