import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [0] * (m + 1)

items = []

for _ in range(n):
    v, c, k = map(int, input().split())

    cnt = 1
    
    # Binary optimization: split the item into powers of 2 to simulate bounded knapsack
    while k > 0:
        use = min(cnt, k)
        items.append((v * use, c * use))
        k -= use
        cnt *= 2 

# Standard 0/1 knapsack using the converted items
for w, s in items:
    for j in range(m, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + s)

print(dp[m])