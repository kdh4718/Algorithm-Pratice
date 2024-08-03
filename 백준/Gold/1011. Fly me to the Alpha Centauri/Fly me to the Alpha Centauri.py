t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    count = 0
    distance = y - x
    crtDistance = 0
    move = 0

    while crtDistance < distance:
        count += 1
        if count % 2 != 0:
            move += 1
        crtDistance += move

    print(count)