import sys
import math
input = sys.stdin.readline

n = int(input())
cnt = 0

dp = [0]*(n+1)
for i in range(1, int(math.sqrt(n))+1):
    dp[i**2] = 1
    
for i in range(1, n+1):
    if dp[i]:
        continue
        
    j = 1
    while j**2 <= i:
        if not dp[i]:
            dp[i] = dp[j**2] + dp[i - j**2]
        else:
            dp[i] = min(dp[i], dp[j**2] + dp[i - j**2])
        j += 1

print(dp[n])