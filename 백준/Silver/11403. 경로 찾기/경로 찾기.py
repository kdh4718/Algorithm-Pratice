from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0]*n
    
    while queue:
        q = queue.popleft()
        for i in range(n):
            if graph[q][i] and check[i] == 0:
                graph[x][i] = 1
                check[i] = 1
                queue.append(i)

    return
            
for i in range(n):
    bfs(i)
        
for i in graph:
    print(*i)