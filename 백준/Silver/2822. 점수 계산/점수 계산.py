#백준 2822 점수 계산

scores = []

for i in range(8):
    score = int(input())
    scores.append((score,i))

scores.sort(reverse=True, key=lambda x: x[0])

top_scores_indices = [index for _, index in scores[:5]]
top_scores_indices.sort()

sum_top_scores = sum(score for score, _ in scores[:5])
result = ' '.join(str(index+1) for index in top_scores_indices)

print(sum_top_scores)
print(result)


