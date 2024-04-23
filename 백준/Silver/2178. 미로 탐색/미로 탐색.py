from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(cur_x, cur_y):
    q = deque()
    q.append((cur_x, cur_y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
        
            if 0 <= new_x < n and 0 <= new_y < m and arr[new_x][new_y] == 1:
                q.append((new_x, new_y))
                arr[new_x][new_y] = arr[x][y] + 1
    
    return arr[-1][-1]
        
print(bfs(0, 0))