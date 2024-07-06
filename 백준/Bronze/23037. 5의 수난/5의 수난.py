#백준 23037: 5의 수난

word = input()

sum = 0

for i in range(5):
    sum += int(word[i]) ** 5

print(sum)

