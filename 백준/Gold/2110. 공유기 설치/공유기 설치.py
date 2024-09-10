n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()
start, end = 0, home[-1] - home[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    loc = home[0]
    cnt = 1

    for i in range(1, len(home)):
        if home[i] >= loc + mid:
            cnt += 1
            loc = home[i]

    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)