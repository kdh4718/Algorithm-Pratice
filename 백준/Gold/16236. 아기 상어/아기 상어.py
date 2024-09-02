from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
size = 2
stack = 0
locX, locY = 0, 0
time = 0

def bfs(i, j):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((i, j, 0))
    visited[i][j] = True
    minimum = float('inf')
    food = []

    while q:
        x, y, t = q.popleft()

        if t > minimum:
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append((nx, ny, t + 1))
                    if 0 < graph[nx][ny] < size:
                        if t + 1 < minimum:
                            minimum = t + 1
                            food = [(nx, ny, t + 1)]
                        elif t + 1 == minimum:
                            food.append((nx, ny, t + 1))

    if food:
        food.sort(key=lambda x: (x[0], x[1]))
        return food[0]
    else:
        return [-1, -1, 0]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            locX, locY = i, j
            graph[i][j] = 0
            break

while True:
    locX, locY, t = bfs(locX, locY)

    if locX == locY == -1:
        break

    graph[locX][locY] = 0
    stack += 1
    if stack == size:
        size += 1
        stack = 0

    time += t

print(time)