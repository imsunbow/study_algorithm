#백준 11478: 서로 다른 부분 문자열의 개수

s = input()
res = set() #중복 비허용

#반복문을 통해 결과값에 삽입
for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i:j+1]
        res.add(temp)
        
cnt = len(res)

#출력
print(cnt)