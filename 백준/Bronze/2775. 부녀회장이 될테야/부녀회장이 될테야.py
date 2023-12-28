#백준 2775: 부녀회장이 될테야

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1,n+1)]

    for _ in range(k):
        for j in range(1,n):
            floor[j] += floor[j-1]

    print(floor[-1])