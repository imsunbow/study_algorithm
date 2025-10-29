#백준 26069: 붙임성 좋은 총총이

n = int(input())
dance = {"ChongChong"}

for _ in range(1,n+1):
    a,b = input().split()

    #set에 추가
    if a in dance:
        dance.add(b)

    if b in dance:
        dance.add(a)

print(len(dance))