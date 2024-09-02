from collections import deque

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    visited = [False]*(n + 1)
    graph = [[0]*(n+1) for _ in range(n+1)]
    count = 0

    def bfs(i):
        visited[i] = True
        q = deque()
        q.append(i)

        while q:
            x = q.popleft()

            for i in range(1, n + 1):
                if graph[x][i] == 1 and not visited[i]:
                    q.append(i)
                    visited[i] = True

    for i in range(m):
        a = list(map(int, input().split()))

        if len(a) > 1:
            graph[a[0]][a[1]] = 1
            graph[a[1]][a[0]] = 1

    for i in range(1, n + 1):
        if not visited[i]:
            count += 1
            bfs(i)

    print(f'#{test_case}', count)
