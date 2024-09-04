from collections import deque

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    dp = [[1e9] * n for _ in range(n)]
    dp[0][0] = graph[0][0]  
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(i, j):
        q = deque()
        q.append((i, j))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    dist = dp[x][y] + graph[nx][ny]
                    if dp[nx][ny] > dist:
                        dp[nx][ny] = dist
                        q.append((nx, ny))

        return

    bfs(0, 0)

    print(f'#{test_case}', dp[-1][-1])
