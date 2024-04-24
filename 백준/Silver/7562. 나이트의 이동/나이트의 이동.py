from collections import deque

n = int(input())
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(x, y):
    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l and not board[nx][ny]:
                board[nx][ny] = board[x][y] + 1
                q.append([nx, ny])

for _ in range(n):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    board = [[0]*l for _ in range(l)]
    
    q = deque([])
    q.append([sx, sy])
    bfs(ex, ey)
    board[sx][sy] = 0
    
    print(board[ex][ey])