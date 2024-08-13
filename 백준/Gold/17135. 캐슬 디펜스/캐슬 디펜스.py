from itertools import combinations as cb

n, m, d = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
maxCount = 0
archer = [0, 1, 2]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move():
    for i in range(n - 1, 0, -1):
        graph[i] = graph[i - 1][:]
    graph[0] = [0] * m

def shoot(x, y):
    target = []
    distance = d+1

    for j in range(d):
        for k in range(n):
            for l in range(m):
                if abs(x - k) + abs(y - l) == j and graph[k][l] == 1:
                    target.append([k, l])
        if target:
            target.sort(key=lambda x: x[1])
            return target[0]

    return [100, 100]

for archer in cb([i for i in range(m)], 3):
    count = 0
    graph = [a[:] for a in g]

    for _ in range(n):
        target = [0] * 3

        for i in range(3):
            target[i] = shoot(n - 1, archer[i])

        for i in range(len(target)):
            targetX = target[i][0]
            targetY = target[i][1]
            if target[i] != [100, 100] and graph[targetX][targetY] != 0:
                graph[targetX][targetY] = 0
                count += 1

        move()
    maxCount = max(maxCount, count)

print(maxCount)
