from collections import deque

for test_case in range(1, 11):
    num, number = map(int, input().split())
    course = list(map(int, input().split()))
    load = [[] for _ in range(100)]
    visited = [False]*100
    flag = False

    for i in range(0, len(course), 2):
        x, y = course[i], course[i+1]
        load[x].append(y)

    def bfs():
        global flag
        q = deque()
        q.append(0)
        visited[0] = True

        while q:
            n = q.popleft()

            for i in load[n]:
                if i == 99:
                    flag = True
                    return

                if not visited[i]:
                    q.append(i)
                    visited[i] = True

        return

    bfs()
    print(f"#{num}", 1 if flag else 0)
