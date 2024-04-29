import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chart = []
for _ in range(n):
    chart.append(list(map(int, input().split())))
    
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + chart[i-1][j-1]
        
for i in range(m):
    sx, sy, ex, ey = map(int, input().split())
    answer = dp[ex][ey] - dp[ex][sy-1] - dp[sx-1][ey] + dp[sx-1][sy-1]
    print(answer)