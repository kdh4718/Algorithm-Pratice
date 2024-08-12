n = int(input())
egg = [list(map(int, input().split())) for _ in range(n)]
maxCrash = 0

def crashEgg(index):
    global maxCrash

    if index == n:
        count = 0
        for e in egg:
            if e[0] <= 0:
                count += 1
        maxCrash = max(maxCrash, count)
        return

    if egg[index][0] <= 0:
        crashEgg(index + 1)
        return

    isCrashed = False
    for i in range(n):
        if i == index or egg[i][0] <= 0:
            continue

        egg[index][0] -= egg[i][1]
        egg[i][0] -= egg[index][1]

        isCrashed = True
        crashEgg(index + 1)

        egg[index][0] += egg[i][1]
        egg[i][0] += egg[index][1]

    if not isCrashed:
        crashEgg(index + 1)

crashEgg(0)
print(maxCrash)
