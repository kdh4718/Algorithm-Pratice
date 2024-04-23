from collections import deque

c = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b, graph, m, n):
    n = len(graph)
    q = deque([(a, b)])
    graph[a][b] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    
    return 

for i in range(c):
    m, n, t = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0
    
    for _ in range(t):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j, graph, m, n)
                cnt += 1
    
    print(cnt)