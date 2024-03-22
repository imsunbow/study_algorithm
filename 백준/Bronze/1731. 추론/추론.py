#백준 1731: 추론

numbers = []
n = int(input())

for _ in range(n):
    number = int(input())
    numbers.append(number)

if numbers[1]- numbers[0] == numbers[2] - numbers[1]:
    difference = numbers[1] - numbers[0]
    ans = numbers[n - 1] + difference
else:
    difference = numbers[1] / numbers[0]
    ans = numbers[n - 1] * difference

print(int(ans))