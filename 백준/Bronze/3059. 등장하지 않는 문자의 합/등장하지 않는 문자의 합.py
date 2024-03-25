#백준 3059: 등장하지 않는 문자의 합

#테스트 케이스 입력
t = int(input())

for _ in range(t):
    sum = 2015
    s = set(input())
    for i in s:
        sum -= ord(i)

    print(sum)

