#백준 7785: 회사에 있는 사람

n = int(input())

people = []

#list 저장
for _ in range(n):
    a,b = input().split()
    if b == 'enter':
        people.append(a)
    elif b == 'leave':
        people.remove(a)

#역순 배열
people.sort(reverse=True)

#출력
for i in people:
    print(i)





