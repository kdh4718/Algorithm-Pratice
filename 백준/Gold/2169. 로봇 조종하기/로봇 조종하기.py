n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, m):
    dp[0][i] += dp[0][i - 1]

for i in range(1, n):
    dpL = dp[i][:]
    dpR = dp[i][:]

    for j in range(m):
        if j == 0:
            dpL[j] += dp[i - 1][j]
        else:
            dpL[j] += max(dp[i - 1][j], dpL[j - 1])

    for j in range(m - 1, -1, -1):
        if j == m - 1:
            dpR[j] += dp[i - 1][j]
        else:
            dpR[j] += max(dp[i - 1][j], dpR[j + 1])

    for j in range(m):
        dp[i][j] = max(dpL[j], dpR[j])

print(dp[-1][-1])
