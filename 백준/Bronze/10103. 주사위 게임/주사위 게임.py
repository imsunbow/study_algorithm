#백준 10103

n = int(input())
score_a = 100
score_b = 100

for _ in range(n):
    roll_a,roll_b = map(int,input().split())
    if roll_a < roll_b:
        score_a -= roll_b
    elif roll_a > roll_b:
        score_b -= roll_a

print(score_a)
print(score_b)

