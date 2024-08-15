from itertools import combinations as cb
from collections import deque

n = int(input())
person = list(map(int, input().split()))
region = [[] for _ in range(n+1)]
minDifference = 1e9

for i in range(1, n+1):
    a, *b = map(int, input().split())
    region[i].extend(b)

def connected(g):
    group = g[:]
    q = deque()
    q.append(group[0])
    group.remove(group[0])

    while q:
        x = q.popleft()

        for num in region[x]:
            if num in group:
                q.append(num)
                group.remove(num)

    return len(group) == 0

for _ in range(1, n):
    for group1 in cb([i for i in range(1, n+1)], _) :
        group1 = list(group1)
        group2 = [i for i in range(1, n+1) if i not in group1]

        if connected(group1) and connected(group2):

            population1 = [person[i - 1] for i in group1]
            population2 = [person[i - 1] for i in group2]
            minDifference = min(minDifference, abs(sum(population1) - sum(population2)))

print(minDifference if minDifference != 1e9 else -1)