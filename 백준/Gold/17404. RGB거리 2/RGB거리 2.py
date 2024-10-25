n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
result = 1e9

for first_color in range(3):
    dp = [[1e9] * 3 for _ in range(n)]
    dp[0][first_color] = costs[0][first_color]

    for i in range(1, n):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

    for last_color in range(3):
        if last_color != first_color:
            result = min(result, dp[n-1][last_color])

print(result)
