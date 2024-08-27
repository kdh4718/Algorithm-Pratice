n = int(input())
m = int(input())
busLine = [[1e9]*(n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    busLine[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    busLine[a][b] = min(busLine[a][b], c)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            busLine[j][k] = min(busLine[j][k], busLine[j][i] + busLine[i][k])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if busLine[i][j] == 1e9:
            print(0, end=" ")
        else:
            print(busLine[i][j], end=" ")
    print()


