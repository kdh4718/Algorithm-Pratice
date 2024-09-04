from collections import deque

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    location = []
    count = 0

    def bfs(a, b):
        q = deque()
        q.append((a, b))
        visited[a][b] = True

        min_x, min_y = a, b
        max_x, max_y = a, b

        while q:
            x, y = q.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

                    max_x = max(max_x, nx)
                    max_y = max(max_y, ny)

        sizeX = max_x - min_x + 1
        sizeY = max_y - min_y + 1
        return sizeX, sizeY


    def calculate_mat(left, right):
        if left == right:
            return 0
        if DP[left][right] != -1:
            return DP[left][right]

        temp_result = float('inf')
        for i in range(left, right):
            temp_result1 = calculate_mat(left, i)
            temp_result2 = calculate_mat(i + 1, right)
            cal_num = sorted_info[left][0] * sorted_info[i][1] * sorted_info[right][1]
            temp_result = min(temp_result, temp_result1 + temp_result2 + cal_num)

        DP[left][right] = temp_result
        return temp_result


    for i in range(n):
        for j in range(n):
            if graph[i][j] and not visited[i][j]:
                x, y = bfs(i, j)
                location.append((x, y))

    mat_info = location

    info_dict = {}
    keys = set()
    values = set()
    for m, n in mat_info:
        info_dict[m] = n
        keys.add(m)
        values.add(n)

    start = keys - values
    start = start.pop()

    sorted_info = []
    while len(sorted_info) < len(mat_info):
        sorted_info.append((start, info_dict[start]))
        start = info_dict[start]

    DP = [[-1] * len(sorted_info) for _ in range(len(sorted_info))]
    result = calculate_mat(0, len(sorted_info) - 1)

    print(f'#{test_case}', result)