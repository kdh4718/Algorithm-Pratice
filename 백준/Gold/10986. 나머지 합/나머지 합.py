import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
count = 0

dp = [0]*m
prefix_sum = 0
for i in range(n):
    prefix_sum += num[i]
    dp[prefix_sum % m] += 1

a = dp[0]
for i in range(m):
    a += dp[i] * (dp[i]-1) // 2
    
print(a)