# 백준 14642: 나는 행복합니다!

n,m,k = map(int, input().split())

n = k//m
m = k%m

print(n, m, end=' ')