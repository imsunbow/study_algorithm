# 백준 4383: 점프는 즐거워

import sys
input = sys.stdin.readline

while True:    
    lst =  list(map(int, input().split()))
    if not lst:
        break
    n = lst[0]
    if n == 0:
        break    
    nums = lst[1:]
    if n == 1:
        print("Jolly")
        continue    
    diffs = set(abs(nums[i] - nums[i-1]) for i in range(1, n)) # calculate differences
    if diffs == set(range(1, n)):
        print("Jolly")
    else:
        print("Not jolly")