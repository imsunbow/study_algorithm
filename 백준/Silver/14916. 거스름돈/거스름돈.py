n = int(input())

for five_coins in range(n // 5, -1, -1):
    remaining = n - five_coins * 5
    
    if remaining % 2 == 0: 
        two_coins = remaining // 2
        print(five_coins + two_coins)
        break
else:
    print(-1)