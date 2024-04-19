#백준 15905: 스텔라가 치킨을 선물했어요

T = int(input())

arr = []

for _ in range(T):
    arr.append(list(map(int,input().split())))

#배열
arr.sort(key= lambda x: [-x[0], x[1]])

#학생 수 계산
cnt = 0
for i in range(T):
    if arr[4][0] == arr[i][0] and arr[4][1] < arr[i][1]:
        cnt += 1

print(cnt)
