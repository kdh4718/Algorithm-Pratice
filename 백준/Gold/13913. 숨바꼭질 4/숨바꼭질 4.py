from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
minTime = 1e9
visited = [-1] * 100001
moves = [0] * 100001
visited[n] = 0

def path(x):
    arr = []
    temp = x
    for _ in range(visited[x] + 1):
        arr.append(temp)
        temp = moves[temp]
    return arr[::-1]

def bfs(s, t):
    global minTime, minCourse
    q = deque()
    q.append((s))

    while q:
        x = q.popleft()

        if x == t:
            minTime = visited[x]
            # minCourse = course
            break

        for move in (x * 2, x + 1, x - 1):
            if 0 <= move <= 100000:

                if visited[move] == -1 or visited[move] > visited[x] + 1:
                    visited[move] = visited[x] + 1
                    q.append(move)
                    moves[move] = x

bfs(n, m)

print(minTime)
print(*path(m))
