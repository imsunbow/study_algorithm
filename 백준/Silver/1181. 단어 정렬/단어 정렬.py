#백준 1181: 단어 정렬

N = int(input())
words = []

for i in range(N):
    word = input()
    words.append(word)

# 중복된 단어를 제거한 후에 길이와 알파벳 순으로 정렬
unique_words = sorted(set(words), key=lambda x: (len(x), x))

for i in unique_words:
    print(i)





