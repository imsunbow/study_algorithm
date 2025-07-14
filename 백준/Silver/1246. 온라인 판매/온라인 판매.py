# 백준 1246 : 온라인 판매

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
prices = [int(input()) for _ in range(m)]
prices.sort()

max_profit = 0 
best_price = 0

for i in range(m):
    price = prices[i]
    buyers = m - i  
    count = min(n, buyers) 
    profit = price * count
    if profit > max_profit:
        max_profit = profit
        best_price = price

print(best_price, max_profit)