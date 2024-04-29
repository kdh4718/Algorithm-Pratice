from collections import deque

n, m = map(int, input().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
q = deque()
graph = [list(map(int, input().split())) for _ in range(n)]
lenght = [[0]*m for _ in range(n)]

def bfs(x, y):
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0:
                if not lenght[nx][ny]:
                    q.append([nx, ny])
                    lenght[nx][ny] = lenght[x][y] + 1
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            lenght[i][j] = 0
            
for i in range(n):
    for j in range(m):
        if not lenght[i][j] and graph[i][j] == 1:
            lenght[i][j] = -1
        
for le in lenght:
    print(*le)