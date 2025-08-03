def count_partitions():
    import sys
    input = sys.stdin.read
    N = int(input())
    total = N * (N + 1) // 2
    if total % 2 != 0:
        print(0)
        return
    
    target = total // 2
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for num in range(1, N+1):
        for k in range(target, num-1, -1):
            dp[k] += dp[k - num]
    
    print(dp[target] // 2)

count_partitions()
