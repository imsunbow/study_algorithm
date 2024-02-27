#백준 1475: 방 번호

#풀이법: set
word = input()
answer = [0] * 10 #공간 할당

for i in range(len(word)): #단어 길이만큼 반복
    n = int(word[i])
    # n == 6,9 처리
    if n == 6 or n == 9:
        if answer[6] <= answer[9]:
            answer[6] += 1
        else:
            answer[9] += 1
    #n != 6,9 처리
    else:
        answer[n] += 1

#출력:
print(max(answer))










