from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b, maps):
    q = deque([(a, b, False, 0)])
    lenX = len(maps)
    lenY = len(maps[0])
    visited = [[[False]*2 for i in range(lenY)] for _ in range(lenX)]
    visited[a][b][0] = True
    
    while q:
        x, y, flag, cnt = q.popleft()
        
        if maps[x][y] == 'E' and flag:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < lenX and 0 <= ny < lenY and maps[nx][ny] != 'X':
                if flag:
                    if not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        
                        q.append((nx, ny, flag, cnt + 1))
                else:
                    if not visited[nx][ny][0]:
                        visited[nx][ny][0] = True
                        
                        if maps[nx][ny] == 'L': 
                            q.append((nx, ny, True, cnt + 1))
                        else:
                            q.append((nx, ny, flag, cnt + 1))   
    
    return -1

def solution(maps):
    maps = [list(map) for map in maps]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                answer = bfs(i, j, maps)
    
    return answer