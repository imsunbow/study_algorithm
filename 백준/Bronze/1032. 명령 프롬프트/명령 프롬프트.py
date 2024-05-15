#백준 1032: 명령 프롬프트

n = int(input())
words = list(input())

for i in range(n - 1):
    word = list(input())
    for j in range(len(words)):
        if words[j] != word[j]:
            words[j] = '?'

print(''.join(words))
