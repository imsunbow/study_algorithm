# 백준 16212: 정열적인 정렬

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

print(*lst)