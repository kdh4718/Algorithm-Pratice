n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
answer = 0

def dfs(x, y, d):
    global answer
    if not visited[x][y]:
        visited[x][y] = True
        answer += 1
    
    for i in range(4):
        nd = (d+3)%4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx, ny, nd)
            return

        d = nd
                
    nd = (d+2)%4
    nx = x + dx[nd]
    ny = y + dy[nd]
    
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        dfs(nx, ny, d)
    
    return

dfs(r, c, d)
print(answer)