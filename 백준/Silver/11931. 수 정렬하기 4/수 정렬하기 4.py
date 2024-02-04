#백준 15688: 수 정렬하기 5

n = int(input())
lst = []

for _ in range(n):
    a = int(input())
    lst.append(a)

lst.sort(reverse=True)

for i in lst:
    print(i)

