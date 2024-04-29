import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[False]*m for _ in range(n)]
count = 0

def dfs(x, y, c, num):
    global count
    if c == 4:
        count = max(count, num)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, c+1, num+graph[nx][ny])
            visited[nx][ny] = False

def exception_tetromino(x, y):
    global count
    for i in range(4):
        tmp = graph[x][y]
        
        for j in range(3):
            t = (i+j)%4
            nx = x + dx[t]
            ny = y + dy[t]
            
            if not (0 <= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += graph[nx][ny]
            
        count = max(count, tmp)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False
        exception_tetromino(i, j)
        
print(count)
