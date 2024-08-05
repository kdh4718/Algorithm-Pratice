from collections import deque

n, k = map(int, input().split())
distance = [-1]*100001
distance[n] = 0
q = deque()
q.append(n)

while q:
    x = q.popleft()

    if x == k:
        break

    if 0 <= x-1 < 100001 and distance[x-1] == -1:
        distance[x-1] = distance[x] + 1
        q.append(x-1)
    if 0 < 2*x < 100001 and distance[x*2] == -1:
        distance[2*x] = distance[x]
        q.append(2*x)
    if 0 <= x+1 < 100001 and distance[x+1] == -1:
        distance[x+1] = distance[x] + 1
        q.append(x+1)

print(distance[k])
