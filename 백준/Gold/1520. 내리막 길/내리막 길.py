import sys
sys.setrecursionlimit(10**8)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    loc = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
            loc += dfs(nx, ny)
            
    dp[x][y] = loc
    
    return dp[x][y]

print(dfs(0, 0))