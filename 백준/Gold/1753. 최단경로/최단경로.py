import heapq
import sys

input = sys.stdin.readline

INF = float('inf')

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
distance[k] = 0

def dijkstra():
    q = []
    heapq.heappush(q, (0, k))

    while q:
        dis, cur = heapq.heappop(q)

        if distance[cur] < dis:
            continue

        for x, y in graph[cur]:
            num = dis + y
            if num < distance[x]:
                distance[x] = num
                heapq.heappush(q, (num, x))

for _ in range(e):
    u, v, x = map(int, input().split())
    graph[u].append([v, x])

dijkstra()

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
