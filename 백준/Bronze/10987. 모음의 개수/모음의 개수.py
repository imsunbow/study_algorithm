#백준 10987: 모듬의 개수

word = input()
vowel = ['a','e','i','o','u']
count = 0

for alphabet in word:
    count += vowel.count(alphabet)

print(count)



