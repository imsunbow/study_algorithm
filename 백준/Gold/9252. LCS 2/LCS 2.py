# 백준 9252: LCS 2

# LCS( 최장 공통 부분 수열 )

import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())

dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
path = []

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(A)][len(B)])

#lcs출력: 재귀

def getText(r,c):
    if r == 0 or c == 0:
        return
    if A[r - 1] == B[c - 1]:
        path.append(A[r - 1])
        getText(r - 1, c - 1) #대각선 위로

    else:
        if dp[r - 1][c] >= dp[r][c - 1]:
            getText(r - 1, c) # 위로
        else:
            getText(r, c - 1)

getText(len(A), len(B))

for i in range(len(path) - 1, -1, -1):
         print(path[i], end='')
print()