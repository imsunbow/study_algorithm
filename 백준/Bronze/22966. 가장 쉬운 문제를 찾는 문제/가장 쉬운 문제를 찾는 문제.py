#백준 22966 : 가장 쉬운 문제를 찾는 문제

n = int(input())
lst = []

for _ in range(n):
    lst.append(input().split())
lst = sorted(lst,key=lambda x:x[1])

print(lst[0][0])



