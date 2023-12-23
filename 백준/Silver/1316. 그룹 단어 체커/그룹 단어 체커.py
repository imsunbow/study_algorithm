#백준 1376: 그룹 단어 체커

N = int(input())
count = N

for _ in range(N):
    word = input()
    for j in range(0,len(word)-1): #인덱스로 for문 돌리기
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count -= 1
            break

print(count)



