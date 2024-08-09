from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
year = 0
count = 0

def bfs(i, j):
    melt = []
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                if graph[nx][ny] == 0 and visited[nx][ny]:
                    melt.append((x, y))

    for x, y in melt:
        graph[x][y] = 0

def meltingPoint(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return

while True:
    visited = [[False]*m for _ in range(n)]
    air = [[False]*m for _ in range(n)]
    currentCount = 0
    meltingPoint(0, 0)

    for i in range(n):
        currentCount += graph[i].count(1)

    if currentCount == 0:
        break
    count = currentCount

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    year += 1

print(year)
print(count)