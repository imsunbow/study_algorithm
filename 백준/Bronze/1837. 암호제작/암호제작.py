# 백준 1837: 암호제작

p,k = map(int, input().split())

for i in range(2, k): # check divisibility from 2 to k-1
    if p % i == 0:
        print("BAD", i) # print "bad" with the first division found
        break
else:
    print("GOOD") # print "good"