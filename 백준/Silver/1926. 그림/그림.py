from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
painting = 0
maxSize = 0

def bfs(i, j):
    count = 1
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1

    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            painting += 1
            maxSize = max(maxSize, bfs(i, j))

if painting:
    print(painting)
    print(maxSize)
else:
    print(0, 0)