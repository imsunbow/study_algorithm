#백준 1015: 수열 정렬

import sys
input = sys.stdin.readline

n = int(input())

original = list(map(int, input().split()))
sorted_original = sorted(original)

used_index = [False] * n
result = []

for value in original:
    for idx in range(n):
        if not used_index[idx] and sorted_original[idx] == value: # check index is used
            result.append(idx) # append index to result list
            used_index[idx] = True # false > true
            break

print(*result) #unpacking