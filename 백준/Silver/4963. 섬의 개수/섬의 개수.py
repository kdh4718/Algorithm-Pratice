import sys
sys.setrecursionlimit(10**4)

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(x, y, h, w, graph, visited):
    visited[x][y] = True
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                dfs(nx, ny, h, w, graph, visited)
    
    return 

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j, h, w, graph, visited)
                cnt += 1
                
    print(cnt)