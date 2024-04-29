n, k = map(int, input().split())
item = [[0, 0] for _ in range(n)]
for i in range(n):
    item[i][0], item[i][1] = map(int, input().split())

dp = [0 for _ in range(k+1)]
for w, v in item:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)
print(dp[-1])