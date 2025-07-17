#백준 12865: 평범한 배낭

n,k = map(int,input().split())
dp = [[0]*(k+1) for _ in range(n+1)]


for i in range(1,n+1):
    w,v = map(int,input().split())
    for j in range(1,k+1): #무게 1->k까지
        if j < w:  #j가 w보다 작으면 
            dp[i][j] = dp[i-1][j] #이전값을 그대로
        else: #j가 w보다 크거나 같으면
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v) #이전값 or 이전값에서 w를 뺀값+현재값 중 큰값으로 업데이트
            
print(dp[n][k])