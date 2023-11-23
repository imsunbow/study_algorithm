# 백준 11557

T = int(input())

for _ in range(T):
    school = []
    drink = []
    N = int(input())
    for _ in range(N):
        a, b = input().split()
        school.append(a)
        drink.append(int(b))
    idx = drink.index(max(drink))
    print(school[idx])



