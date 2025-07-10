# 백준 17127 : 벚꽃이 정보섬에 피어난 이유

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = 0

for i in range(1, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a = 1
            for x in range(0, i):
                a *= nums[x]
            b = 1
            for x in range(i, j):
                b *= nums[x]
            c = 1
            for x in range(j, k):
                c *= nums[x]
            d = 1
            for x in range(k, n):
                d *= nums[x]
            ans = max(ans, a + b + c + d)
print(ans)