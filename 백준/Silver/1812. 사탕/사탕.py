#백준 1812: 사탕

n = int(input())
s = 0
lst = []

#1번 값 출력
for i in range(n):
    lst.append(int(input()))
    s += lst[i] * (-1)**i #짝수 인덱스는 더하고 홀수 인덱스는 빼준다
a = s // 2
print(a)

#2번~마지막까지 값 구하기
for i in range(n-1):
    a = lst[i] - a
    print(a)
