# 백준 33612: 피갤컵

n = int(input())

y = 2024
m = 8 + 7 * (n - 1) # increase month by input value

while m > 12:
    y += 1
    m -= 12

print(y, m)