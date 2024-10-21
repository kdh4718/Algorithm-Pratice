import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])

start, end = map(int, input().split())
dist = [1e9] * (n + 1)
path = [-1] * (n + 1)

def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, point = heapq.heappop(q)
        if cost > dist[point]:
            continue

        for e, c in graph[point]:
            new_cost = c + cost

            if new_cost < dist[e]:
                dist[e] = new_cost
                path[e] = point
                heapq.heappush(q, (new_cost, e))

    return dist[end]

def get_path(end):
    result = []
    while end != -1:
        result.append(end)
        end = path[end]
    return result[::-1]

minCost = dij(start)
minCourse = get_path(end)
minCity = len(minCourse)

print(minCost)
print(minCity)
print(*minCourse)
