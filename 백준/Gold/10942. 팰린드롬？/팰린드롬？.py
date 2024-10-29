import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [[False] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = True

for i in range(n - 1):
    if num[i] == num[i + 1]:
        dp[i][i + 1] = True

for i in range(3, n + 1):
    for j in range(n - i + 1):
        k = i + j - 1
        if num[j] == num[k] and dp[j + 1][k - 1]:
            dp[j][k] = True

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())

    print(1 if dp[s - 1][e - 1] else 0)
