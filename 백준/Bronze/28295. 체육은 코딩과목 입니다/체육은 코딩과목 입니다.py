#백준 28295: 체육은 코딩과목입니다

counts = []

for _ in range(10):
    a = int(input())
    counts.append(a)

total_sum = sum(counts)

#출력

if total_sum % 4 == 3:
    print("W")
elif total_sum % 4 == 2:
    print("S")
elif total_sum % 4 == 1:
    print("E")
else:
    print("N")