# 백준 1043: 거짓말

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
know = set(input().split()[1:]) 
people = []

for _ in range(m):
    people.append(set(input().split()[1:])) # append the list of people who are at each party


# count the number of people who knows I'm lying
for _ in range(m):
    for person in people:
        if person & know: # if person knows someone who is lying
            know = know.union(person) # add them to the set of liars

cnt = 0
for person in people:
    if person & know: # if no one at the party knows a liar
        continue 
    cnt += 1

print(cnt)