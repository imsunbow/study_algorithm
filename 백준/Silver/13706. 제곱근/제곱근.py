import sys

input = sys.stdin.readline

n = int(input())

left, right = 1, n
result = -1

while left <= right:
    mid = (left + right) // 2
    if mid * mid == n:
        result = mid
        break
    elif mid * mid < n:
        left = mid + 1
    else:
        right = mid - 1
                
print(result)

# this code below makes tle
# input = sys.stdin.readline

# n = int(input())

# # print number * number == n using brute force
# for i in range(1, n + 1):
#     if i * i == n:
#         print(i)
#         break