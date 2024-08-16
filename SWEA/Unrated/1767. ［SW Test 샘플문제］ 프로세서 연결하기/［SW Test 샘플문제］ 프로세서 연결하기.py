t = int(input())

for _ in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    process = []
    maxCpu = 0
    minLine = 1e9
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def connect(x, y, d, graph):
        nx = x
        ny = y
        flag = True

        while True:
            nx += dx[d]
            ny += dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 0:
                    flag = False
                    break
            else:
                break

        if not flag:
            return -1

        count = 0
        while True:
            x += dx[d]
            y += dy[d]

            if 0 <= x < n and 0 <= y < n:
                count += 1
                graph[x][y] = 2
            else:
                break

        return count

    def dfs(index, core, line, g):
        global maxCpu, minLine

        if index >= len(process):
            if core > maxCpu:
                maxCpu = core
                minLine = line
            elif core == maxCpu:
                minLine = min(minLine, line)

            return

        graph = [i[:] for i in g]

        for i in range(4):
            gr = [i[:] for i in g]
            num = connect(process[index][0], process[index][1], i, gr)
            if num == -1:
                continue
            dfs(index + 1, core + 1, line + num, gr)

        dfs(index + 1, core, line, graph)
        # dfs(index + 1, core, line, graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                if 1 <= i < n-1 and 1 <= j < n-1:
                    process.append([i, j])

    dfs(0, 0, 0, graph)
    print(f"#{_}", minLine)