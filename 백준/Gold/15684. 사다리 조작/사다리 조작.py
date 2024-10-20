import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
graph = [[False] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = True

def check():
    for i in range(n):
        startPoint = i

        for j in range(h):
            if graph[j][startPoint]:
                startPoint += 1
            elif startPoint > 0 and graph[j][startPoint - 1]:
                startPoint -= 1

        if i != startPoint:
            return False

    return True

def draw(depth, x, y):
    if depth > 3:
        return -1

    if check():
        return depth

    result = -1
    for i in range(x, h):
        k = y if i == x else 0

        for j in range(k, n - 1):
            if not graph[i][j] and (j == 0 or not graph[i][j - 1]) and (j == n - 1 or not graph[i][j + 1]):
                graph[i][j] = True
                temp = draw(depth + 1, i, j + 2)

                if temp != -1:
                    if result == -1 or temp < result:
                        result = temp

                graph[i][j] = False

    return result

answer = draw(0, 0, 0)
print(answer if answer != -1 else -1)
