from itertools import combinations

t = int(input())

for test_case in range(1, t+1):
    n, m, c = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    maximum = 0

    def maxBee(honeys):
        totalHoney = 0

        for i in range(1, len(honeys)+1):
            for honey in combinations(honeys, i):
                honey = list(honey)
                if sum(honey) > c:
                    continue
                sumHoney = sum([i*i for i in honey])
                totalHoney = max(totalHoney, sumHoney)

        return totalHoney

    def bees(honey, x, y):
        global maximum
        secondMax = 0
        for i in range(m):
            visited[x][y+i] = True

        beeA = maxBee(honey)

        for i in range(n):
            for j in range(n - m + 1):
                if not any(visited[i][j:j + m]):
                    beeB = maxBee(graph[i][j:j+m])
                    secondMax = max(secondMax, beeB)

        maximum = max(maximum, beeA + secondMax)

    for i in range(n):
        for j in range(n-m+1):
            visited = [[False] * n for _ in range(n)]

            bees(graph[i][j:j+m], i, j)

    print(f'#{test_case}', maximum)