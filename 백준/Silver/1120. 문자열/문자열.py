# 백준 1120: 문자열

word_a,word_b = input().split()

a_len = len(word_a)
b_len = len(word_b)
min_diff = a_len

for i in range(b_len - a_len + 1):
    diff = 0
    for j in range(a_len):
        if word_a[j] != word_b[i + j]:
            diff += 1
    if diff < min_diff:
        min_diff = diff

print(min_diff)