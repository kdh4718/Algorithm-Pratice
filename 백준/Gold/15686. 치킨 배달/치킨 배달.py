from itertools import combinations

n, m = map(int, input().split())
home, chicken = [], []
visited = [False]*n
minNum = 1e9

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if row[j] == 1:
            home.append([i, j])
        elif row[j] == 2:
            chicken.append([i, j])

for i in combinations(chicken, m):
    length = 0
    for j in home:
        currentLen = 1e9
        for k in range(m):
            currentLen = min(currentLen, abs(i[k][0] - j[0]) + 
                            abs(i[k][1] - j[1]))

        length += currentLen
    minNum = min(minNum, length)

print(minNum)