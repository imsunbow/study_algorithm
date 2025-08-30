scores = [int(input()) for _ in range(10)]
total, res = 0, 0

for score in scores:
    total += score
    if abs(100 - total) < abs(100 - res):
        res = total
    elif abs(100 - total) == abs(100 - res):
        res = max(res, total)        
print(res)