#백준 2587 대표값2

numbers = []

for _ in range(5):
    a = int(input())
    numbers.append(a)


numbers.sort()
print(int(sum(numbers)/5))
print(numbers[2])