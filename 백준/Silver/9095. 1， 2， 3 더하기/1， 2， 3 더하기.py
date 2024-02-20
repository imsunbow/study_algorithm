#백준 9095 : 1,2,3 더하기

def add_count(n):
    dp = [0] * (n+1) #배열 저장
    dp[0] = 1 #초기값 세팅

    #반복문을 통한 출력
    for i in range(1,n+1):
        dp[i] += dp[i-1] #1을 더하는 경우
        if i >= 2:
            dp[i] += dp[i-2] #2를 더하는 경우
        if i >= 3:
            dp[i] += dp[i-3] #3을 더하는 경우

    return dp[n]

t = int(input())

for _ in range(t):
    n = int(input())
    result = add_count(n)
    print(result)