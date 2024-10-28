a = [""] + list(input())
b = [""] + list(input())
dp = [[0] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])

lcs = []
i, j = len(a) - 1, len(b) - 1
while i > 0 and j > 0:
    if a[i] == b[j]:
        lcs.append(a[i])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print("".join(reversed(lcs)))
