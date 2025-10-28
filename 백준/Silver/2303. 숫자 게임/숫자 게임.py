import sys
from itertools import combinations as comb

input = sys.stdin.readline

personal_max_num = []

n = int(input())

for _ in range(n):
    personal_card = []
    card_lst= list(map(int, input().split()))

    card_comb = list(comb(card_lst, 3))
    personal_card.append(max(sum(comb) % 10 for comb in card_comb))
    personal_max_num.append(personal_card[0])

highest_score_players = []

for i in range(len(personal_max_num)):
    if personal_max_num[i] == max(personal_max_num):
        highest_score_players.append(i + 1) # save index

print(max(highest_score_players))