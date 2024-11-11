from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()


def moveJ(x, y, c):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == ".":
                graph[nx][ny] = "J"
                q.append((nx, ny, c + 1))

    return


def moveF(x, y, c):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == "." or graph[nx][ny] == "J":
                graph[nx][ny] = "F"
                q.append((nx, ny, c + 1))

    return


def check(x, y, c):
    if x == 0 or x == n - 1 or y == 0 or y == m - 1:
        print(c)
        exit()


for i in range(n):
    for j in range(m):
        if graph[i][j] == "J":
            q.append((i, j, 1))
            break

for i in range(n):
    for j in range(m):
        if graph[i][j] == "F":
            q.append((i, j, 1))

while q:
    x, y, c = q.popleft()

    if graph[x][y] == "J":
        check(x, y, c)
        moveJ(x, y, c)
    else:
        moveF(x, y, c)

print("IMPOSSIBLE")
