# 백준 2455 지능형 기차

people = 0
max_people = 0

for _ in range(4):
    a,b = map(int,input().split())
    people += b-a
    if people> max_people:
        max_people = people

print(max_people)