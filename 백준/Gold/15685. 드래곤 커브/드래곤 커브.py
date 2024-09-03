n = int(input())
graph = [[False]*101 for _ in range(101)]
curve = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
count = 0

for y, x, d, g in curve:
    dragon = [d]
    graph[x][y] = True
    for i in range(g):
        tail = []
        for j in dragon:
            tail.append((j + 1) % 4)

        dragon.extend(tail[::-1])

    for dra in dragon:
        x += dx[dra]
        y += dy[dra]

        graph[x][y] = True

for i in range(100):
    for j in range(100):
        if graph[i][j]:
            if graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
                count += 1

print(count)
