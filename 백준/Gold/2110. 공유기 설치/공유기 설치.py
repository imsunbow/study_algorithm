import sys

input = sys.stdin.readline

n, c = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(n)]

home.sort()

# get the place to fix the connector which is the maxium distance

# check whether or not we can install the connector
def can_install(distance):
    count = 1 
    last_position = home[0][0] # initialize the last position

    for i in range(1, n):
        if home[i][0] - last_position >= distance:
            count += 1
            last_position = home[i][0]
            if count == c: # we cannot install more than c
                return True

    return False

# bs to find the maximum distance
def binary_search():
    left = 1
    right = home[-1][0] - home[0][0] 
    answer = 0  

    while left <= right:
        mid = (left + right) // 2

        if can_install(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

print(binary_search())