from collections import deque

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    location = []


    def bfs(a, b):
        q = deque()
        q.append((a, b))
        visited[a][b] = True

        min_x, min_y = a, b
        max_x, max_y = a, b

        while q:
            x, y = q.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

                    max_x = max(max_x, nx)
                    max_y = max(max_y, ny)

        sizeX = max_x - min_x + 1
        sizeY = max_y - min_y + 1
        return sizeX, sizeY


    for i in range(n):
        for j in range(n):
            if graph[i][j] and not visited[i][j]:
                x, y = bfs(i, j)
                location.append([x, y])

    location.sort(key=lambda x: (x[0] * x[1], x[0]))

    print(f'#{test_case}', len(location), end=' ')
    for loc in location:
        print(*loc, end=' ')
    print()
