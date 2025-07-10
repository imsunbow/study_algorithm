# 백준 23881 : 알고리즘 수업1

import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n-1,0,-1):
    index = i
    for j in range(i-1, -1, -1):
        if arr[j] > arr[index]:
            index = j
    if index != i:
        arr[i], arr[index] = arr[index], arr[i] # swap
        cnt += 1
        if cnt == k:
            print(arr[index],arr[i])
            sys.exit()
print(-1)
