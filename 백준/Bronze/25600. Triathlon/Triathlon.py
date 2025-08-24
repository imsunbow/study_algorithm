n = int(input())

max_score = 0

for _ in range(n):
    a, d, g = map(int, input().split())
    score = a * (d + g) if a != d + g else a * 2 * (d + g)
    max_score = max(max_score, score) 
    
print(max_score)