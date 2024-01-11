#백준 2563: 색종이

import sys
input = sys.stdin.readline
result = 0

paper = [[0] * 101 for _ in range(101)]

#입력값
for _ in range(int(input())):
    a,b = map(int,input().split())

#색종이 넓이 구하기
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j] = 1 

#결과값 출력
for i in paper:
    result += sum(i)

print(result)




