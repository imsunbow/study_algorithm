import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_lst = list(map(int, input().split()))

prefix_sum = [0]
total = 0

for num in num_lst:
    total += num
    prefix_sum.append(total)
    
for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])