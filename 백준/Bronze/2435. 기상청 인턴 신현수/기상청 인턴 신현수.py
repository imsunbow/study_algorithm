#백준 2435: 기상청 인턴 신현수

n,k = map(int,input().split())
lst = list(map(int,input().split()))

sum_v = 0
max_v = -float('inf') #초기값을 음의 무한대로 설정

for i in range(n-k+1):
    sum_v = 0
    for j in range(k):
        sum_v += lst[i+j]
    max_v = max(sum_v,max_v)

print(max_v)
