n = int(input())
for _ in range(n):
    num = int(input())
    dp = [1]*(num+2)
    for i in range(3, num+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[num-1])