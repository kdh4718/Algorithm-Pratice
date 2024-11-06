n = int(input())
flower = [list(map(int, input().split())) for _ in range(n)]
count, index, maxEnd = 0, 0, (0, 0)
now, end = (3, 1), (11, 30)

flower.sort()

while True:
    flag = False

    for i in range(index, n):
        if (flower[i][0], flower[i][1]) > now: break

        if now >= (flower[i][0], flower[i][1]) and (flower[i][2], flower[i][3]) > maxEnd:
            flag = True
            index = i
            maxEnd = (flower[i][2], flower[i][3])

    if not flag:
        print(0)
        break

    count += 1
    now = maxEnd
    if now > end:
        print(count)
        break