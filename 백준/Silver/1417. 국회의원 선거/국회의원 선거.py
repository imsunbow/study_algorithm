import sys

input = sys.stdin.readline

n = int(input())
votes = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
else:
    cnt = 0
    while True:
        max_vote = max(votes[1:])
        if votes[0] > max_vote:
            print(cnt)
            break
        idx = 1 + votes[1:].index(max_vote)
        votes[idx] -= 1
        votes[0] += 1
        cnt += 1