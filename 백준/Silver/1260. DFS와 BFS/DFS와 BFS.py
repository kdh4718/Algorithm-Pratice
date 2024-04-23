from collections import deque
n, m, v = map(int, input().split())
graph = [[False]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end = " ")
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[v][i]:
            dfs(i)
    
def bfs(v):
    q = deque([v])
    visited_bfs[v] = True
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            if not visited_bfs[i] and graph[v][i]:
                q.append(i)
                visited_bfs[i] = True
    

dfs(v)
print()
bfs(v)