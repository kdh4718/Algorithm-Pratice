for test_case in range(1, 11):
    num = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    maxNumber = -1e9
    dialeft, diaright = [], []

    for i in range(100):
        col = sum([j[i] for j in graph])
        maxNumber = max(maxNumber, max(col, sum(graph[i])))

        dialeft.append(graph[i][i])
        diaright.append(graph[99-i][99-i])

    maxNumber = max(maxNumber, max(sum(dialeft), sum(diaright)))

    print(f"#{num}", maxNumber)