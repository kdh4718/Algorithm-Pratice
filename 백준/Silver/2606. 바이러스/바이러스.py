from collections import deque

c = int(input())
n = int(input())
graph = [[False]*(c+1) for _ in range(c+1)]
visited = [False]*(c+1)

for i in range(n):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for i in range(1, c+1):
            if not visited[i] and graph[v][i]:
                q.append(i)
                visited[i] = True

bfs(1)
print(visited.count(True)-1)