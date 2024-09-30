import heapq

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))
v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [1e9] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


origin = dijkstra(1)
v1Path = dijkstra(v1)
v2Path = dijkstra(v2)

v1Length = origin[v1] + v1Path[v2] + v2Path[v]
v2Length = origin[v2] + v2Path[v1] + v1Path[v]

result = min(v1Length, v2Length)
print(result if result < 1e9 else -1)
