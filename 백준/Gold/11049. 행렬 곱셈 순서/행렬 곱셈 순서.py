n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n) for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if i + j == n:
            break
            
        dp[j][i+j] = int(1e9)
            
        for k in range(j, i+j):
            dp[j][i+j] = min(dp[j][i+j],dp[j][k] + dp[k+1][i+j] + matrix[j][0]*matrix[k][1]*matrix[i+j][1])

print(dp[0][n-1])