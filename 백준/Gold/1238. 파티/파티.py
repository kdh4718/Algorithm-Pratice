import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, n, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))

    return dist

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist_from_x = dijkstra(x, n, graph)

max_dist = 0
for i in range(1, n + 1):
    if i != x:
        dist_to_x = dijkstra(i, n, graph)[x]
        max_dist = max(max_dist, dist_from_x[i] + dist_to_x)

print(max_dist)
