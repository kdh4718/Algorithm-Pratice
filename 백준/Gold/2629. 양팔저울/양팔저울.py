n = int(input())
weight = list(map(int, input().split()))
t = int(input())
marble = list(map(int, input().split()))
answer = []

dp = [[0 for _ in range((500*i)+1)] for i in range(n+1)]

def cal(num, w):
    if num > n:
        return
    
    if dp[num][w] == 1:
        return
    
    dp[num][w] = 1
    
    cal(num+1, w + weight[num-1])
    cal(num+1, w)
    cal(num+1, abs(w - weight[num-1]))
    
cal(0, 0)

for m in marble:
    if m > 500*n:
        answer.append('N')
    elif dp[n][m] == 1:
        answer.append('Y')
    else:
        answer.append('N')
        
print(*answer)