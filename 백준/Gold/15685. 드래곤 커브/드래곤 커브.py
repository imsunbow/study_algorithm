#백준 15685: 드래곤 커브

#입력값
N = int(input())
arr = [[0] * 101 for _ in range(101)]

di = [0,-1,0,1]
dj = [1,0,-1,0]


for _ in range(N): #드래곤커브 입력
    sj,si,dr,g = map(int,input().split())
    lst = [(si,sj)] #시작점
    lst.append((si+di[dr],sj+dj[dr]))
    for _ in range(g):
        # 끝좌표 기준으로 90도 회전
        ei,ej = lst[-1]
        for i in range(len(lst)-2,-1,-1):
            ci,cj = lst[i]
            lst.append((ei-(ej-cj),ej+(ei-ci)))

    #arr에 드래곤커브 표시
    for i,j in lst:
        arr[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1] ==1:
            ans+=1
print(ans)


