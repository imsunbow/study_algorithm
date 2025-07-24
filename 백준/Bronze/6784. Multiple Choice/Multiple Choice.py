# 백준 6784 : multiple choice

n = int(input())
stu_lst = []
ans_lst = []
cnt = 0

for _ in range(n):
    stu_lst.append(input())
                   
for _ in range(n):
    ans_lst.append(input())
    
for i in range(n):
    if stu_lst[i] == ans_lst[i]:
        cnt += 1
        
print(cnt)