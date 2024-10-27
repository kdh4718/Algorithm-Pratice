import heapq

n, m = map(int, input().split())
degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

heap = []
for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    current = heapq.heappop(heap)
    result.append(current)
    
    for next in graph[current]:
        degree[next] -= 1
        if degree[next] == 0:
            heapq.heappush(heap, next)

print(" ".join(map(str, result)))
