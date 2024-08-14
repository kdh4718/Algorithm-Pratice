def check():
    blind = 0
    for g in graph:
        blind += g.count(0)
    return blind

def change(graph, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = -1

def cctvCheck(c, graph):
    global blindSpot
    if c == len(cctv):
        count = 0
        for i in range(n):  
            count += graph[i].count(0)
        blindSpot = min(blindSpot, count)
        return

    tmpGraph = [i[:] for i in graph]
    num, x, y = cctv[c]

    for i in mode[num]:
        change(tmpGraph, i, x, y)
        cctvCheck(c + 1, tmpGraph)
        tmpGraph = [i[:] for i in graph]

    return

n, m = map(int, input().split())
graph = []
cctv = []
blindSpot = 1e9
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]], ]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

cctvCheck(0, graph)

print(blindSpot)