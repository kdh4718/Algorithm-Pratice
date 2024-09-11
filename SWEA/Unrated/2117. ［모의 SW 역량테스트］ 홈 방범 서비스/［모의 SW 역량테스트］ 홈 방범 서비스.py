from collections import deque

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    cost = [i * i + (i - 1) * (i - 1) for i in range(26)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    maxCount = 0

    def bfs(i, j):
        global maxCount
        q = deque()
        q.append((i, j))
        scope = 1
        count = graph[i][j]
        visited[i][j] = True

        if count * m - cost[scope] >= 0:
            maxCount = max(count, maxCount)

        while scope < n+1:
            length = len(q)

            for _ in range(length):
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        count += graph[nx][ny]

            if count * m - cost[scope + 1] >= 0:
                maxCount = max(count, maxCount)

            scope += 1

        return

    for i in range(n):
        for j in range(n):
            visited = [[False] * n for _ in range(n)]
            bfs(i, j)

    print(f'#{test_case}', maxCount)
