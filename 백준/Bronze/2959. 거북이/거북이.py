# 백준 2959: 거북이 

lst = list(map(int, input().split()))
lst.sort()

print(lst[0] * lst[2])  