n, k = map(int, input().split())

min_rating = 0
max_rating = 0

for _ in range(k):
    cur_rating = int(input())
    min_rating += cur_rating
    max_rating += cur_rating
    
min_rating = (min_rating + (n - k) * -3) / n
max_rating = (max_rating + (n - k) * 3) / n

print(min_rating, max_rating)