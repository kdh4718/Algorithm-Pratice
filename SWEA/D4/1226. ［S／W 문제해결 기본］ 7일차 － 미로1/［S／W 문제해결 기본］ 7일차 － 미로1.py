from collections import deque

for test_case in range(1, 11):
    n = int(input())
    maze = [list(input()) for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    flag = False

    def bfs(i, j):
        global flag

        q = deque()
        q.append((i, j))

        while q:
            x, y = q.popleft()

            if int(maze[x][y]) == 3:
                flag = True
                break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 16 and 0 <= ny < 16 and int(maze[nx][ny]) != 1:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

    for i in range(16):
        for j in range(16):
            if int(maze[i][j]) == 2:
                bfs(i, j)

    print(f"#{n}", 1 if flag else 0)