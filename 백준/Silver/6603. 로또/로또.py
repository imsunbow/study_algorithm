#백준 6603: 로또

import itertools

while True:

    #입력값
    numbers = list(map(int,input().split()))

    #k와 S지정
    k = numbers[0]
    S = numbers[1:]

    for i in itertools.combinations(S,6): #itertools 라이브러리 활용하여 combination 적용
        print(*i)
    print() #공백열 생성 (문제 조건)

    if k == 0:
        exit()


