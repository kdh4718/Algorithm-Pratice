from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
maxDistance = 0

def bfs(i, j):
    global maxDistance
    q = deque()
    q.append((i, j, 0))
    visited[i][j] = True

    while q:
        x, y, d = q.popleft()
        maxDistance = max(maxDistance, d)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L':
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, d+1))

    return

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[False]*m for _ in range(n)]
            bfs(i, j)

print(maxDistance)