#백준 1268: 임시 반장 정하기

N = int(input())
students = []
same = [0] * N

for i in range(N):
    students.append(list(map(int,input().split())))
    same[i] = [0] * N

for i in range(5): #1학년
    for j in range(N): #j번의 1학년
        for k in range(j+1,N): #k번의 1학년 (j번의 1학년과 비교)

            if students[j][i] == students[k][i]: #같으면 1개씩 더하기
                same[k][j] = 1
                same[j][k] = 1

cnt = []

#출력을 위한 입력
for l in same:
    cnt.append(l.count(1))

#출력
print(cnt.index(max(cnt)) + 1)






