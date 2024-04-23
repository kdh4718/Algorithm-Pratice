n = int(input())
line = [[0, 0] for _ in range(n)]
for i in range(n):
    line[i][0], line[i][1] = map(int, input().split())

dp = [1]*n
line.sort()
for i in range(1, n):
    for j in range(0, i):
        if line[j][1] < line[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))