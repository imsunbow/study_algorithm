#백준 8979: 올림픽

#테스크케이스 입력
n,k = map(int,input().split())
medals = []

#메달 입력
for _ in range(n):
    medal = list(map(int,input().split()))
    medals.append(medal)

#메달 정렬
medals.sort(key=lambda x: (x[1],x[2],x[3]),reverse=True)

#순위 구하기
grade, s = 1,0

for i in range(n):
    if i !=0:
        if medals[i-1][1:] == medals[i][1:]:
            s += 1
        else:
            if s:
                grade += s
                s = 0
            grade += 1
    if medals[i][0] == k:
        print(grade)
        break



