# 백준 1377: 버블 소트 

import sys
input = sys.stdin.readline

n = int(input())
arr = [(int(input()), i) for i in range(n)]  
arr.sort()  # sort by the first element (the value)

max_index = 0

for i in range(n):
    max_index = max(max_index, arr[i][1] - i) # update maximum index difference
print(max_index + 1)