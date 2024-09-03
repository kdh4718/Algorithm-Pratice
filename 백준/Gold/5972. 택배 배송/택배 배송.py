import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [1e9] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)

        if dist > distance[cur]:
            continue

        for next in graph[cur]:
            cost = dist + next[1]

            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(1)

print(distance[-1])
