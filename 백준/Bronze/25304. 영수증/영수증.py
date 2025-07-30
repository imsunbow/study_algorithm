x = int(input())
n = int(input())

sum_price = 0

for _ in range(n):
    price, quantity = map(int, input().split())
    sum_price += price * quantity
    
print("Yes" if sum_price == x else "No")