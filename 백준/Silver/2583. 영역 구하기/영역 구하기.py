import sys
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
cnt = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, count):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            if not graph[nx][ny]:
                count = max(count, bfs(nx, ny, count + 1))
    
    return count

for i in range(k):
    sx, sy, ex, ey = map(int, input().split())
    
    for i in range(sy, ey):
        for j in range(sx, ex):
            graph[i][j] = 1

for i in range(m):
    for j in range(n):
        if not graph[i][j] and not visited[i][j]:
            cnt.append(bfs(i, j, 1))
            
print(len(cnt))  
print(*sorted(cnt))