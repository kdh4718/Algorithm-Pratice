l = int(input())
n = int(input())
visited = [False] * (l + 1)
maxWant, maxGet = 0, 0
wantNum, getNum = 0, 0

for i in range(1, n + 1):
    s, e = map(int, input().split())
    if (abs(e - s) > maxWant):
        maxWant = abs(e - s)
        wantNum = i

    count = 0
    for j in range(s, e+1):
        if not visited[j]:
            count += 1
            visited[j] = True

    if count > maxGet:
        maxGet = count
        getNum = i

print(wantNum)
print(getNum)