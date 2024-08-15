from itertools import combinations as cb
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virus = []
minimumTime = 1e9
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(q):
    visited = [[False]*n for _ in range(n)]
    time = 0
    empty = sum(row.count(0) for row in graph)

    while q:
        x, y, c = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    empty -= 1
                    time = c + 1
                q.append((nx, ny, c + 1))

    return time if not empty else 1e9

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i, j])

for i in cb(virus, m):
    q = deque()

    for x, y in i:
        q.append((x, y, 0))

    count = bfs(q)
    minimumTime = min(minimumTime, count)

print(minimumTime if minimumTime != 1e9 else -1)
