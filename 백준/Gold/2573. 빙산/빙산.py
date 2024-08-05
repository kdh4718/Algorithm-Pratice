from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(i, j, visited):
    q = deque([(i, j)])
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))

def melt_icebergs():
    melt_list = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                count = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        count += 1
                if count > 0:
                    melt_list.append((i, j, count))

    for x, y, count in melt_list:
        graph[x][y] = max(0, graph[x][y] - count)

year = 0
while True:
    visited = [[False] * m for _ in range(n)]
    region_count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                region_count += 1

    if region_count == 0:
        year = 0
        break
    if region_count > 1:
        break

    melt_icebergs()
    year += 1

print(year)
