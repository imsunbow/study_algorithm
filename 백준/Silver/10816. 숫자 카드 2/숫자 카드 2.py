#백준 10816: 숫자 카드 2

#풀이법: 딕셔너리

#필요 라이브러리 호출
import sys

#입력값
n = int(input())
cards = list(map(int,sys.stdin.readline().split()))
m = int(input())
checks = list(map(int,sys.stdin.readline().split()))

#오름차순 정렬
cards.sort()

dic = {}

#딕셔너리에 카드 추가
for x in cards:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

#출력
for x in checks:
    if x in dic:
        print(dic[x],end=' ')
    else:
        print('0',end=' ')

