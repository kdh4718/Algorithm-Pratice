from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = set()
locRed = []
locBlue = []
count = 1e9


def move(x, y, d):
    flag = False

    while True:
        x += dx[d]
        y += dy[d]

        if graph[x][y] == '#':
            x -= dx[d]
            y -= dy[d]
            break

        if graph[x][y] == 'O':
            flag = True
            break

    return x, y, flag


def bfs(redLoc, blueLoc):
    global count

    q = deque()
    q.append([redLoc, blueLoc, 0])

    while q:
        red, blue, time = q.popleft()

        if time > 10:
            continue

        for i in range(4):
            nxR, nyR, flagR = move(red[0], red[1], i)
            nxB, nyB, flagB = move(blue[0], blue[1], i)

            if nxR == nxB and nyR == nyB:
                if red[0] * dx[i] + red[1] * dy[i] > blue[0] * dx[i] + blue[1] * dy[i]:
                    nxB -= dx[i]
                    nyB -= dy[i]
                else:
                    nxR -= dx[i]
                    nyR -= dy[i]

            if flagB:
                continue
            if flagR:
                count = min(count, time + 1)
                return
            if (nxR, nyR, nxB, nyB) not in visited:
                visited.add((nxR, nyR, nxB, nyB))
                q.append(([nxR, nyR], [nxB, nyB], time + 1))

    return


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            locRed = [i, j]
        if graph[i][j] == 'B':
            locBlue = [i, j]

bfs(locRed, locBlue)

print(count if count <= 10 else -1)
