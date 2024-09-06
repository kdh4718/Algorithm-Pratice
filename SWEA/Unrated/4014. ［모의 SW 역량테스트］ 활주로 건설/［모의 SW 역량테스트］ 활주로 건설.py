t = int(input())

for test_case in range(1, t+1):
    n, l = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    def climb(roads):
        global count
        last = roads[0]
        used = [False] * n

        for i in range(1, len(roads)):
            if last == roads[i]:
                continue
            elif last + 1 == roads[i]:
                if i - l < 0:
                    return

                for j in range(i - l, i):
                    if last != roads[j] or used[j]:
                        return
                    used[j] = True

                last = roads[i]

            elif last - 1 == roads[i]:
                if i + l > n:
                    return

                for j in range(i, i + l):
                    if roads[i] != roads[j] or used[j]:
                        return
                    used[j] = True

                last = roads[i]

            else:
                return

        count += 1

    for i in range(n):
        road = grid[i]
        climb(road)

        road = [grid[j][i] for j in range(n)]
        climb(road)

    print(f'#{test_case}', count)