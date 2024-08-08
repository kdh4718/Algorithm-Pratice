T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    maxHegiht = 0
    maxCourse = 0
    top = []

    def dfs(x, y, course, dig):
        global maxCourse

        maxCourse = max(maxCourse, course)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] < graph[x][y]:
                    visited[x][y] = True
                    dfs(nx, ny, course + 1, dig)
                    visited[x][y] = False
                elif dig:
                    if graph[nx][ny] - graph[x][y] + 1 <= dig:
                        visited[x][y] = True
                        temp = graph[nx][ny]
                        graph[nx][ny] = graph[x][y] - 1
                        dfs(nx, ny, course + 1, 0)
                        graph[nx][ny] = temp
                        visited[x][y] = False

        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] > maxHegiht:
                maxHegiht = graph[i][j]
                top = [[i, j]]
            elif graph[i][j] == maxHegiht:
                top.append([i, j])

    for i, j in top:
        visited = [[False] * n for _ in range(n)]
        visited[i][j] = True
        dfs(i, j, 1, k)

    print(f"#{test_case}", maxCourse)
