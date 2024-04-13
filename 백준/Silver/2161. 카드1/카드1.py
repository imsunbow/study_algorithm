#백준 2161: 카드1

from collections import deque

n = int(input())
cards = deque(list(range(1,n+1)))

trash = []

while cards:
    #카드 버리기 후 쓰레기통에 카드 삽입
    card = cards.popleft()
    trash.append(card)
    #카드 목록의 최하단에 카드 삽입
    if cards:
        card = cards.popleft()
        cards.append(card)

print(*trash)





