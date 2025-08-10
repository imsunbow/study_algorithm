from itertools import combinations

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

for comb in combinations(nums, m):
    print(' '.join(map(str, comb)))