count = 1

while True:
    n = int(input())
    if n == 0: exit()
    name = [input() for _ in range(n)]
    dic = dict()

    for _ in range(2*n - 1):
        a, b = map(str, input().split())
        a = int(a)

        if name[a-1] not in dic:
            dic[name[a-1]] = 1
        else:
            del dic[name[a-1]]

    print(count, *list(dic.keys()))
    count += 1