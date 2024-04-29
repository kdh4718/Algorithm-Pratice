from collections import deque

n, m = map(int, input().split())
visited = [False]*101
graph = [0]*101
ladder = dict()
snake = dict()

for i in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
    
for i in range(m):
    x, y = map(int, input().split())
    snake[x] = y
    
def bfs():
    q = deque([1])
    visited[1] = True
    
    while q:
        pos = q.popleft()
        
        for i in range(1, 7):
            next_pos = pos + i
            
            if next_pos < 101 and not visited[next_pos]:
                if next_pos in ladder:
                    next_pos = ladder[next_pos]
                    
                if next_pos in snake:
                    next_pos = snake[next_pos]
                    
                if not visited[next_pos]:
                    q.append(next_pos)
                    visited[next_pos] = True
                    graph[next_pos] = graph[pos] + 1
    
    return

bfs()
print(graph[-1])