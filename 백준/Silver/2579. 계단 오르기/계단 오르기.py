#백준 2579: 계단 오르기

#계단 수
n = int(input())

#빈 리스트 생성
lst = []

for _ in range(n):
    stair = int(input())
    lst.append(stair)

dp = [0] * n

#출력
if len(lst)<=2: #계단이 2개 이하
    print(sum(lst))
else: #계단 수 > 3일 때
    dp[0] = lst[0] #첫번째 계단
    dp[1] = lst[0] + lst[1] #두번째 계단

    for i in range(2,n): #3번째 계단 ~
        dp[i] = max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])
    #출력    
    print(dp[-1])










