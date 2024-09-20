n, m, length = map(int, input().split())
graph = [list(input()) for _ in range(n)]
count = 0
visited = [[False]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, l):
    global count

    if x == 0 and y == m-1:
        if l == length:
            count += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'T':
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, l+1)
                visited[nx][ny] = False

    return

visited[n-1][0] = True
dfs(n-1, 0, 1)
print(count)