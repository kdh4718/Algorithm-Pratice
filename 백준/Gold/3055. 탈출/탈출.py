from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            q.append((i, j, 1))

for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            q.append((i, j, 1))

while q:
    x, y, c = q.popleft()

    if graph[x][y] == 'S':
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'D':
                    print(c)
                    exit()
                if graph[nx][ny] == '.':
                    graph[nx][ny] = 'S'
                    q.append((nx, ny, c + 1))
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 'X' and graph[nx][ny] != 'D' and graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                    q.append((nx, ny, c + 1))

print("KAKTUS")
