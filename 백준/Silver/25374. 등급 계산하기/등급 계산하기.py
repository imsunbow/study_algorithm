n = int(input())
scores = list(map(int, input().split()))

scores.sort(reverse=True)

cuts = [0, 4, 7, 12, 17, 20, 17, 12, 7, 4]
answer = [0] * 10

grade = 1
answer[grade] += 1
cuts[grade] -= 1

for i in range(1, n):
    if cuts[grade] == 0:
        if scores[i] == scores[i-1]:
            next_grade = grade + 1
            while cuts[next_grade] == 0:
                next_grade += 1
            cuts[grade] += 1
            cuts[next_grade] -= 1
        else:
            next_grade = grade + 1
            while cuts[next_grade] == 0:
                next_grade += 1
            grade = next_grade

    answer[grade] += 1
    cuts[grade] -= 1

for g in range(1, 10):
    print(answer[g])