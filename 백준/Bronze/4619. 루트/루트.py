while True:
    B, N = map(int, input().split())
    if B == 0 and N == 0:
        break

    i = 0

    while i ** N < B:
        i += 1

    
    print(i if (i ** N) - B < B - ((i - 1) ** N)  else i - 1) # print closest
