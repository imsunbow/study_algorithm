n = int(input())
friends = list(map(str, input().split()))
mine = input()

cnt = 0

for i in range(n):
    if friends[i] == mine:
        cnt += 1

print(cnt)