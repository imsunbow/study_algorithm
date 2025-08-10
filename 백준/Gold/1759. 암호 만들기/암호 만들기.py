from itertools import combinations

l, c = map(int, input().split())
words = list(map(str, input().split()))

words.sort()

for comb in combinations(words, l):
    vowel_count = sum(1 for char in comb if char in 'aeiou')
    consonant_count = l - vowel_count

    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(comb))