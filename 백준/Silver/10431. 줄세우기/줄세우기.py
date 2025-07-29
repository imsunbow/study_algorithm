t = int(input())

for i in range(t):
    lst = list(map(int, input().split()))
    height_lst = lst[1:]
    cnt = 0
    line = []
    
    for h in height_lst:
        for j in range(len(line)):
            if line[j] > h:
                line.insert(j, h)
                cnt += len(line) - j - 1 
                break
        else:
            line.append(h)
    
    print(lst[0], cnt)