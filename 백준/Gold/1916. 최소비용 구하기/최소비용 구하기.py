import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
busLine = [[] for _ in range(n+1)]
distance = [1e9]*(n+1)

def bfs(start):
    q = []
    heapq.heappush(q, [0, start])

    while q:
        dis, x = heapq.heappop(q)

        if distance[x] < dis:
            continue

        for s, c in busLine[x]:
            num = dis + c
            if num < distance[s]:
                distance[s] = num
                heapq.heappush(q, [num, s])

for _ in range(m):
    s, e, c = map(int, input().split())
    busLine[s].append([e, c])

start, end = map(int, input().split())
distance[start] = 0
bfs(start)

print(distance[end])