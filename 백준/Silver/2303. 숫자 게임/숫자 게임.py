from itertools import combinations as comb

N = int(input())
max_num = []

for _ in range(N):
    check = []
    card = list(map(int,input().split()))
    numbers = list(comb(card, 3))
    for num in numbers :
        c = sum(num) % 10 # calculate mod 10
        check.append(c)
    max_num.append(max(check))


check_max = []

for i in range(len(max_num)):
    if max_num[i] == max(max_num) :
        check_max.append(i + 1) # calculate player number

print(max(check_max))