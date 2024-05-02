#백준 1026: 보물

n = int(input())
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))

lst1.sort()
lst2.sort(reverse=True)

#답 초기화
result = 0
for i in range(n):
    result += lst1[i] * lst2[i]

print(result)