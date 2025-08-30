a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

price_x = a * p
price_y = b if p <= c else b + d * (p - c)

print(min(price_x, price_y))