from itertools import combinations

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    minimun = 1e18

    def sumTaste(case):
        taste = 0

        for i in case:
            for j in range(n):
                if j in case:
                    taste += graph[i][j]

        return taste

    for case in combinations([i for i in range(n)], n//2):
        caseA = list(case)
        caseB = [i for i in range(n) if i not in caseA]
        tasteA = sumTaste(caseA)
        tasteB = sumTaste(caseB)

        minimun = min(minimun, abs(tasteA - tasteB))

    print(f'#{test_case}', minimun)

