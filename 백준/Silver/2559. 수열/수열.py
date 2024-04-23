n, k = map(int, input().split())
tem = list(map(int, input().split()))
max_tem = -1e9
sum_tem = [0]*(n+1)
sum_tem[1] = tem[0]

for i in range(2, n+1):
    sum_tem[i] = tem[i-1] + sum_tem[i-1]
for i in range(0, n-k+1):
    max_tem = max(max_tem, sum_tem[i+k] - sum_tem[i])
print(max_tem)