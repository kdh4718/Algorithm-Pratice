r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
airCleaner = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move(top, bottom):
    # 공기청정기 위쪽 순환
    for i in range(top-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for i in range(c-1):
        graph[0][i] = graph[0][i+1]
    for i in range(top):
        graph[i][c-1] = graph[i+1][c-1]
    for i in range(c-1, 1, -1):
        graph[top][i] = graph[top][i-1]
    graph[top][1] = 0

    # 공기청정기 아래쪽 순환
    for i in range(bottom+1, r-1):
        graph[i][0] = graph[i+1][0]
    for i in range(c-1):
        graph[r-1][i] = graph[r-1][i+1]
    for i in range(r-1, bottom, -1):
        graph[i][c-1] = graph[i-1][c-1]
    for i in range(c-1, 1, -1):
        graph[bottom][i] = graph[bottom][i-1]
    graph[bottom][1] = 0

def spread(dust, x, y):
    miniDust = graph[x][y] // 5
    spread_count = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
            dust[nx][ny] += miniDust
            spread_count += 1

    dust[x][y] -= miniDust * spread_count
    return dust

for i in range(r):
    if graph[i][0] == -1:
        airCleaner.append(i)

for _ in range(t):
    dust = [[0] * c for _ in range(r)]
    for j in range(r):
        for k in range(c):
            if graph[j][k] not in [-1, 0]:
                dust = spread(dust, j, k)

    for j in range(r):
        for k in range(c):
            graph[j][k] += dust[j][k]

    move(airCleaner[0], airCleaner[1])

result = 0
for i in range(r):
    result += sum(graph[i])

print(result + 2)