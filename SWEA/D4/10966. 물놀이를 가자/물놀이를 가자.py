from collections import deque

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [list(input().strip()) for _ in range(n)]
    dp = [[1e9] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]


    def bfs(queue):
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if dp[nx][ny] > dp[x][y] + 1:
                        dp[nx][ny] = dp[x][y] + 1
                        queue.append((nx, ny))


    queue = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'W':
                dp[i][j] = 0
                queue.append((i, j))

    bfs(queue)

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L':
                answer += dp[i][j]

    print(f"#{test_case} {answer}")