from collections import deque

t = int(input())

for test_case in range(1, t+1):
    n, *li = list(map(int, input().split()))
    graph = [li[i:i + n] for i in range(0, len(li), n)]
    distCount = [0]*n

    def bfs(a):
        count = [0 if _ == a else 1e9 for _ in range(n)]
        q = deque()
        q.append((a, 1))
        visited[a] = True

        while q:
            x, c = q.popleft()

            for i in range(n):
                if graph[x][i] and not visited[i]:
                    visited[i] = True
                    count[i] = c
                    q.append((i, c+1))

        return sum(count)

    for i in range(n):
        visited = [False]*n
        distCount[i] = bfs(i)

    print(f'#{test_case}', min(distCount))