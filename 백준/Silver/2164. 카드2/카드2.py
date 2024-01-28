#백준 2164: 카드 2

from collections import deque

#입력값
N = int(input())
deque = deque([i for i in range(1,N+1)])


#카드 한 장 남을 떄까지 반복
while(len(deque) > 1):
    deque.popleft() #가장 왼쪽 원소 버리기
    count = deque.popleft() #다음 원소도 제거, count 변수에 추가
    deque.append(count) #count 변수에 추가 후 오른쪽 끝에 두기


print(deque[0]) #0번 인덱스 출력


