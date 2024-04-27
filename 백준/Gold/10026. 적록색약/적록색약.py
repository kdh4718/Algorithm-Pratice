import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
normal_visited = [[False]*(n) for _ in range(n)]
blind_visited = [[False]*(n) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
normal_cnt, blind_cnt = 0, 0

def normal_dfs(x, y):
    color = graph[x][y]
    normal_visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not normal_visited[nx][ny] and graph[nx][ny] == color:
                normal_dfs(nx, ny)
    return

def blind_dfs(x, y):
    color = graph[x][y]
    blind_visited[x][y] = True
    
    if color == 'B':
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not blind_visited[nx][ny] and graph[nx][ny] == color:
                    blind_dfs(nx, ny)
        
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not blind_visited[nx][ny] and graph[nx][ny] != 'B':
                    blind_dfs(nx, ny)
        
    return

for i in range(n):
    for j in range(n):
        if not normal_visited[i][j]:
            normal_dfs(i, j)
            normal_cnt += 1
            
for i in range(n):
    for j in range(n):
        if not blind_visited[i][j]:
            blind_dfs(i, j)
            blind_cnt += 1

print(normal_cnt, blind_cnt)