#백준 24416: 알고리즘 수업 - 피보나치 수 1

def fib(n, cnt1):
    if n == 1 or n == 2:
        cnt1[0] += 1
        return 1
    else:
        return fib(n - 1, cnt1) + fib(n - 2, cnt1) #재귀

def fib_dp(n, cnt2):
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt2[0] += 1  #DP
    return dp[n]

cnt1 = [0]  #재귀
cnt2 = [0]  #DP

#입출력
n = int(input())
fib(n,cnt1)
fib_dp(n,cnt2)

print(cnt1[0],cnt2[0])