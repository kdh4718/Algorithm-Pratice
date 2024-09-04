t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    scr = list(map(int, input().split()))
    screw = [[scr[i], scr[i+1]] for i in range(0, len(scr), 2)]
    maximum = []

    def connect(x, s):
        global maximum

        for i in range(len(screw)):
            if not visited[i] and screw[x][1] == screw[i][0]:
                visited[i] = True
                ss = s[:]
                ss.extend(screw[i])
                connect(i, ss)
                visited[i] = False

        if len(s) > len(maximum):
            maximum = s[:]

        return

    for i in range(len(screw)):
        visited = [False] * n
        visited[i] = True
        connect(i, screw[i])


    print(f'#{test_case}', *maximum)