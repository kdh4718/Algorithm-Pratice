from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split()))for _ in range(n)]for _ in range(h)]
cnt = 0
dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
q = deque([])

def bfs(): 
    while q:
        z, y, x = q.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append([nz, ny, nx])

def check(cnt):
    for grap in graph:
        for gra in grap:
            for gr in gra:
                if gr == 0:
                    return -1
            cnt = max(cnt, max(gra))
    return cnt-1
                
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i, j, k])

bfs()
cnt = check(cnt)
print(cnt)