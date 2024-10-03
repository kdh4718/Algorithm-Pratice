import heapq


def dij(s):
    dist = [1e9] * (n + 1)
    dist[s] = 0
    h = []
    heapq.heappush(h, [s, 0])

    while h:
        point, curD = heapq.heappop(h)

        if curD > dist[point]:
            continue

        for target, newD in graph[point]:
            length = curD + newD

            if length < dist[target]:
                dist[target] = length
                heapq.heappush(h, [target, length])
    return dist


n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
maximum = 0
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

for i in range(1, n + 1):
    dist = dij(i)
    collect = 0
    for j in range(1, n + 1):
        if dist[j] <= m:
            collect += items[j - 1]

    maximum = max(maximum, collect)

print(maximum)
