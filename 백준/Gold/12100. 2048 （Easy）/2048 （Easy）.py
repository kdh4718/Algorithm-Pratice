import copy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
maxNumber = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(graph, direction):
    if direction == 0:
        for j in range(n):
            temp = [graph[i][j] for i in range(n) if graph[i][j] != 0]
            for i in range(1, len(temp)):
                if temp[i] == temp[i - 1]:
                    temp[i - 1] *= 2
                    temp[i] = 0 
            temp = [x for x in temp if x != 0]
            for i in range(n):
                if i < len(temp):
                    graph[i][j] = temp[i]
                else:
                    graph[i][j] = 0
    elif direction == 1:
        for j in range(n):
            temp = [graph[i][j] for i in range(n) if graph[i][j] != 0]
            for i in range(len(temp) - 1, 0, -1):
                if temp[i] == temp[i - 1]:
                    temp[i] *= 2
                    temp[i - 1] = 0
            temp = [x for x in temp if x != 0]
            for i in range(n):
                if i < len(temp):
                    graph[n - 1 - i][j] = temp[len(temp) - 1 - i]
                else:
                    graph[n - 1 - i][j] = 0
    elif direction == 2:
        for i in range(n):
            temp = [graph[i][j] for j in range(n) if graph[i][j] != 0]
            for j in range(1, len(temp)):
                if temp[j] == temp[j - 1]:
                    temp[j - 1] *= 2
                    temp[j] = 0
            temp = [x for x in temp if x != 0]
            for j in range(n):
                if j < len(temp):
                    graph[i][j] = temp[j]
                else:
                    graph[i][j] = 0
    elif direction == 3:
        for i in range(n):
            temp = [graph[i][j] for j in range(n) if graph[i][j] != 0]
            for j in range(len(temp) - 1, 0, -1):
                if temp[j] == temp[j - 1]:
                    temp[j] *= 2
                    temp[j - 1] = 0
            temp = [x for x in temp if x != 0]
            for j in range(n):
                if j < len(temp):
                    graph[i][n - 1 - j] = temp[len(temp) - 1 - j]
                else:
                    graph[i][n - 1 - j] = 0
    return graph


def countMax(graph):
    return max([max(row) for row in graph])


def dfs(graph, count):
    global maxNumber
    if count == 5:
        maxNumber = max(maxNumber, countMax(graph))
        return
    for i in range(4):
        new_graph = copy.deepcopy(graph)
        new_graph = move(new_graph, i)
        dfs(new_graph, count + 1)


dfs(graph, 0)
print(maxNumber)
