for test_case in range(1, 11):
    num = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    visitied = [[False]*100 for _ in range(100)]
    dx, dy = [0, 0, -1], [-1, 1, 0]
    start = graph[-1].index(2)
    location = -1

    def dfs(x, y):
        global location
        visitied[x][y] = True

        if x == 0 and location == -1:
            location = y
            return

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and graph[nx][ny] == 1:
                if not visitied[nx][ny]:
                    dfs(nx, ny)

    dfs(99, start)
    print(f"#{num}", location)