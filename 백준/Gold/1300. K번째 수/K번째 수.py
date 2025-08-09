import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

def count_less_equal(x):
    count = 0
    for i in range(1, n + 1):
        count += min(x // i, n)
    return count

left, right = 1, n * n
answer = 0

# bs
while left <= right:
    mid = (left + right) // 2
    
    if count_less_equal(mid) >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)