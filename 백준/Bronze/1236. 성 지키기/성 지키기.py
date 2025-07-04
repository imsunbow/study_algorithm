#백준 1236: 성 지키기

n,m = map(int,input().split())
guard = [input().strip() for _ in range(n)]

row = 0
for i in range(n):
    if 'X' not in guard[i]:
        row += 1

col = 0
for j in range(m):
    if all(guard[i][j] != 'X' for i in range(n)): 
        col += 1

print(max(row,col))