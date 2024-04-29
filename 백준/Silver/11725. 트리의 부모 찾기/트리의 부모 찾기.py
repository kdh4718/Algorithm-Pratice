import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
root = [0]*(n+1)

def dfs(a):
    for i in graph[a]:
        if not root[i]:
            root[i] = a
            dfs(i)
    
    return

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs(1)
    
for i in range(2, n+1):
    print(root[i])