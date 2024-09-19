n = int(input())
graph = [list(input().split()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
flag = False
teacher = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check():
    for tx, ty in teacher:
        for i in range(4):
            nx, ny = tx, ty

            for j in range(n):
                nx += dx[i]
                ny += dy[i]
                if not (0 <= nx < n and 0 <= ny < n):
                    break
                if visited[nx][ny]:
                    break

                if graph[nx][ny] == 'S':
                    return False

    return True

def dfs(count):
    global flag

    if count == 0:
        if check():
            flag = True
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X' and not visited[i][j]:
                visited[i][j] = True
                dfs(count-1)
                visited[i][j] = False

    return

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append([i, j])

dfs(3)

print("YES" if flag else "NO")