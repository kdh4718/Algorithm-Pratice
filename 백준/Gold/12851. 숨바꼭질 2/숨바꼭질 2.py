from collections import deque

n, m = map(int, input().split())
minTime, minCount = 1e9, 0
visited = [-1] * 100001
visited[n] = 0

def bfs(s, t):
    global minTime, minCount
    q = deque()
    q.append(s)

    while q:
        x = q.popleft()

        if x == t:
            if visited[x] == minTime:
                minCount += 1
            elif visited[x] < minTime:
                minTime = visited[x]
                minCount = 1
            continue

        for move in (x - 1, x + 1, x * 2):
            if move < 0 or move > 100000: continue

            if visited[move] == -1 or visited[move] == visited[x] + 1:
                visited[move] = visited[x] + 1
                q.append(move)

    return


bfs(n, m)

print(minTime)
print(minCount)
