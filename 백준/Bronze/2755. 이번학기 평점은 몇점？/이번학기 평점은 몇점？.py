#백준 2755: 이번학기 평점은 몇점?

sum = 0
rate = 0

rating = {"A+": 4.3, "A0": 4.0, "A-":3.7, "B+": 3.3, "B0": 3.0, "B-":2.7, "C+": 2.3, "C0": 2.0, "C-":1.7, "D+": 1.3, "D0": 1.0, "D-":0.7, "F": 0.0}

N = int(input())
for _ in range(N):
    subject, score, grade = input().split()
    rate += float(score) * rating[grade]
    sum += float(score)

total_grade = rate/sum

print("%.2f" % (round(total_grade + 10**-10, 2)))