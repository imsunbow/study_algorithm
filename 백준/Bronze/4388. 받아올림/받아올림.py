while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    carry = 0 # temp variable to count carries
    count = 0 

    a = str(a).zfill(max(len(str(a)), len(str(b))))
    b = str(b).zfill(max(len(str(a)), len(str(b))))

    for x, y in zip(reversed(a), reversed(b)):
        if int(x) + int(y) + carry > 9: 
            count += 1
            carry = 1
        else:
            carry = 0

    print(count)