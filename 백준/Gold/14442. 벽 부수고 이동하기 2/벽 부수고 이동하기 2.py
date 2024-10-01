from collections import deque
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0][0] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque([(0, 0, 0, 1)])

    while q:
        x, y, wall_broken, dist = q.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and wall_broken < k and not visited[nx][ny][wall_broken + 1]:
                    visited[nx][ny][wall_broken + 1] = True
                    q.append((nx, ny, wall_broken + 1, dist + 1))
                elif graph[nx][ny] == 0 and not visited[nx][ny][wall_broken]:
                    visited[nx][ny][wall_broken] = True
                    q.append((nx, ny, wall_broken, dist + 1))

    return -1


print(bfs())
