# bitmask

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))

arr_left = arr[:N // 2]
arr_right = arr[N // 2:]

def get_subset_sums(nums):
    n = len(nums)
    sums = []
    for bit in range(1 << n):  
        total = 0
        for i in range(n):
            if bit & (1 << i):  
                total += nums[i]
        sums.append(total)
    return sums

sum_left = get_subset_sums(arr_left)
sum_right = get_subset_sums(arr_right)

sum_left.sort()
sum_right.sort()


answer = 0
j = len(sum_left) - 1

for s in sum_right:
    while j >= 0 and s + sum_left[j] > C:
        j -= 1
    answer += j + 1

print(answer)
