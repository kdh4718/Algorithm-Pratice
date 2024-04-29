import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
cnt = 0

def dfs(a):
    visited[a] = True
    for i in graph[a]:
        if not visited[i]:
            dfs(i)
    return

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
        
print(cnt)