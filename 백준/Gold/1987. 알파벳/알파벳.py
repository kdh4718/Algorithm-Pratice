import sys
sys.setrecursionlimit(10**4)

r, c = map(int, input().split())
alp = [list(map(str, input())) for _ in range(r)]
visited = [False]*26

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_cnt = 0

def bfs(x, y, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    visited[ord(alp[x][y])-65] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[ord(alp[nx][ny])-65]:
                bfs(nx, ny, cnt+1)
                visited[ord(alp[nx][ny])-65] = False
    
bfs(0, 0, 1)
print(max_cnt)