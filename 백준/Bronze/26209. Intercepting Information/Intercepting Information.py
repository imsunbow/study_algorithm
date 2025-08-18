nums = list(map(int, input().split()))
print('S' if all(num in (0, 1) for num in nums) else 'F')