T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1]*n for _ in range(n)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    count = -1
    roomNumber = float('inf')

    def dfs(x, y):
        if dp[x][y] != -1:
            return dp[x][y]

        dp[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] + 1:
                    dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

        return dp[x][y]

    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                dfs(i, j)
            if dp[i][j] > count or (dp[i][j] == count and graph[i][j] < roomNumber):
                count = dp[i][j]
                roomNumber = graph[i][j]

    print(f"#{test_case}", roomNumber, count)
