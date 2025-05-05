#백준 1019: 책 페이지

n = int(input())
num = [0] * 10
start = 1
end = n
factor = 1

#start가 end보다 작거나 같을 때까지 반복
while start <= end: #start가 end보다 작거나 같을 때까지 반복
    while start % 10 != 0 and start <= end: #start가 10으로 나누어 떨어지지 않고 start가 end보다 작거나 같을 때까지 반복
        for i in str(start): #start 값 str으로 변환 후 대입
            num[int(i)] += factor
        start += 1 #이동
    if start > end: #start가 end보다 크면 반복문 종료
        break
    while end % 10 != 9 and start <= end: #end가 9로 나누어 떨어지지 않고 start가 end보다 작거나 같을 때까지 반복
        for i in str(end): #end값 변환 후 대입
            num[int(i)] += factor #num에 factor값 대입
        end -= 1 #이동
        
    start //= 10 #start를 10으로 나눈 몫을 대입
    end //= 10 #end를 10으로 나눈 몫을 대입
    
    for i in range(10): #0부터 9까지 반복
        num[i] += (end - start + 1) * factor
    factor *= 10 

#출력
for i in num:
    print(i, end=' ')