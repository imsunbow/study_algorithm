# # 백준 9461: 파도반 수열

# f(n) = f(n-2) + f(n-3) 이용하여 풀이
# 10번 lst값까지는 문제에서 주어짐, 나머지 점화식 넣음
# dp 안써도 될 듯.

import sys
input = sys.stdin.readline

#tc
t = int(input())
lst = [0,1,1,1,2,2,3,4,5,7,9]

for i in range(11,101):
    lst.append(lst[i-2]+lst[i-3])

#입출력
for _ in range(t):
    n = int(input())
    print(lst[n])