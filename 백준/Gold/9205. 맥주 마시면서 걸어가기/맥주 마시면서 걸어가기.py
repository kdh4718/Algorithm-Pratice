from collections import deque

t = int(input())

for test_case in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    point = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))
    visited = [False]*n
    lenght = [0]*n
    flag = False

    def bfs(i, j):
        global flag

        q = deque()
        q.append((i, j))

        while q:
            x, y = q.popleft()

            if abs(end[0] - x) + abs(end[1] - y) <= 1000:
                flag = True
                break

            for i in range(n):
                if not visited[i]:
                    dist = abs(point[i][0] - x) + abs(point[i][1] - y)
                    if dist <= 1000:
                        q.append(point[i])
                        visited[i] = True

        return

    bfs(start[0], start[1])



    print("happy" if flag else "sad")