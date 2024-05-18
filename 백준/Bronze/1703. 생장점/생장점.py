#백준 1703: 생장점

while True:
    lst = list(map(int,input().split()))
    #초기값 세팅
    leaf = 1

    #루프 탈출
    if lst[0] == 0:
        break

    #반복문
    for i in range(1,len(lst),2):
        leaf = (leaf * lst[i]) - lst[i+1]
        
    print(leaf)
