n, k = map(int, input().split())
coin = [0]*n
for i in range(n):
    coin[i] = int(input())
    
count = 0
for i in range(n-1, -1, -1):
    count += k//coin[i]
    k %= coin[i]

print(count)