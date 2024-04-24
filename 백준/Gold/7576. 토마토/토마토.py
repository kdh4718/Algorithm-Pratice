from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque([])

def bfs(): 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

def check(cnt):
    for row in graph:
        for r in row:
            if r == 0:
                return -1
        cnt = max(cnt, max(row))
    return cnt-1
                
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

bfs()
cnt = check(cnt)
print(cnt)