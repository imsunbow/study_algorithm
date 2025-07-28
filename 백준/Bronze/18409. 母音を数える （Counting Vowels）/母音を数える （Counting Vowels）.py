dic_vowel = {'a', 'e', 'i', 'o', 'u'}

n = int(input())
word = input().strip()

total = 0

for i in range(n):
    if word[i] in dic_vowel:
        total += 1
        
print(total)