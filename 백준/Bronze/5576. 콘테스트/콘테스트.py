#백준 5576 : 콘테스트

scores_team1 = []
scores_team2 = []

for _ in range(10):
    score = int(input())
    scores_team1.append(score)

for _ in range(10):
    score = int(input())
    scores_team2.append(score)

top_score_team1 = sum(sorted(scores_team1, reverse=True)[:3])
top_score_team2 = sum(sorted(scores_team2, reverse=True)[:3])

print(top_score_team1, top_score_team2)