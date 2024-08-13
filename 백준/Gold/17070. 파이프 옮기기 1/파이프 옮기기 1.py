n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 가로 ,새로, 대각선
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

def check(i, j):
    pipe = dp[i][j]
    dx = [1, 1, 0]
    dy = [1, 0, 1]
    flag = True

    if j+1 < n and graph[i][j+1] != 1:
        dp[i][j + 1][0] += (pipe[0] + pipe[2])

    for k in range(3):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx >= n or ny >= n or graph[nx][ny] == 1:
            flag = False

    if flag:
        dp[i+1][j+1][2] += sum(pipe)

    if i+1 < n and graph[i+1][j] != 1:
        dp[i+1][j][1] += (pipe[1] + pipe[2])

    return

for i in range(n):
    for j in range(n):
        if graph[i][j] != 1:
            check(i, j)

print(sum(dp[-1][-1]))