# 백준 34052: 체육은 수학과목입니다 2

sum = 0

for _ in range(4):
    sum += int(input())

sum += 300

if sum <= 1800:
    print("Yes")
else:
    print("No")