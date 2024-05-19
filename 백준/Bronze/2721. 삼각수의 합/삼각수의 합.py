#백준 2721: 삼각수의 합

for _ in range(int(input())):
    n = int(input())
    #output
    wn = []
    for k in range(1,n+1):
        range_sum = sum(range(1, k+2))
        wn.append(k*range_sum)
    print(sum(wn))