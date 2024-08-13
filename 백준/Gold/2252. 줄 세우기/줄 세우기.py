from collections import deque

n, m = map(int, input().split())
parent = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
line = []
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    parent[b] += 1

for i in range(1, n+1):
    if parent[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    line.append(x)

    for i in graph[x]:
        parent[i] -= 1
        if parent[i] == 0:
            q.append(i)

print(*line)
