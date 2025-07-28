import sys
input = sys.stdin.readline

s = input().strip()
q = int(input())

count = [[0] * (len(s) + 1) for _ in range(26)] # make table in advance

for i in range(1, len(s) + 1):
    char_idx = ord(s[i - 1]) - ord('a')
    for j in range(26):
        count[j][i] = count[j][i - 1]
    count[char_idx][i] += 1

for _ in range(q):
    alpha, l, r = input().split()
    l = int(l)
    r = int(r)
    idx = ord(alpha) - ord('a')
    print(count[idx][r + 1] - count[idx][l])