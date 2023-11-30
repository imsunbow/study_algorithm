# 백준 2460 지능형 기차2

people = 0
max_people = 0

for _ in range(10):
    a,b = map(int,input().split())
    people += b-a
    if people> max_people:
        max_people = people

print(max_people)