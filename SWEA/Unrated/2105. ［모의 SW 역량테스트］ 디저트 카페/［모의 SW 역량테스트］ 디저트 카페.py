t = int(input())

# 0 : 오른아래, 1 : 왼아래
# 2 : 오른위  3 : 왼위
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

for test_case in range(1, t + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    count = -1


    def check(x, y):
        left = 0
        right = 0

        dicL = {graph[x][y]: 1}
        dicR = {graph[x][y]: 1}

        nx, ny = x, y
        for i in range(n):
            nx += dx[1]
            ny += dy[1]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] not in dicL:
                    left += 1
                    dicL[graph[nx][ny]] = 1
                else:
                    break
            else:
                break

        nx, ny = x, y
        for i in range(n):
            nx += dx[0]
            ny += dy[0]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] not in dicR:
                    right += 1
                    dicR[graph[nx][ny]] = 1
            else:
                break

        return left, right


    def makeCourse(left, right):
        course = []

        for i in range(1, left + 1):
            for j in range(1, right + 1):
                c = [dx[0], dy[0]] * j + [dx[1], dy[1]] * i + [dx[3], dy[3]] * j + [dx[2], dy[2]] * i
                course.append(c)

        return course


    def checkCourse(course, a, b):
        testCount = -1

        for case in course:
            if len(case) // 2 <= testCount: continue
            dic = dict()
            x, y = a, b
            flag = True

            for i in range(0, len(case), 2):
                x += case[i]
                y += case[i + 1]

                if 0 <= x < n and 0 <= y < n:
                    if graph[x][y] not in dic:
                        dic[graph[x][y]] = 1
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break

            if flag:
                testCount = max(testCount, len(case) // 2)

        return testCount


    for i in range(n):
        for j in range(n):
            left, right = check(i, j)

            if left == 0 or right == 0: continue

            course = makeCourse(left, right)

            count = max(count, checkCourse(course, i, j))

    print(f'#{test_case}', count)
