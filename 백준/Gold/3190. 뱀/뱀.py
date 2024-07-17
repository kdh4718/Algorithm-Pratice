from collections import deque

n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
turn = [list(map(str, input().split())) for _ in range(l)]
graph = [[0]*n for _ in range(n)]
location = [[0, 1], [1, 0], [0, -1], [-1, 0]]
snake = deque([[0, 0]])
head = 0
cnt = 0
turnTime = 0
graph[0][0] = 2

for apple in apples:
    graph[apple[0]-1][apple[1]-1] = 1

while True:
    cnt += 1
    
    x, y = snake[0]
    nx = x + location[head][0]
    ny = y + location[head][1]

    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 2:
        if graph[nx][ny] == 1:
            snake.appendleft([nx, ny])
            graph[nx][ny] = 2
        else:
            snake.appendleft([nx, ny])
            graph[nx][ny] = 2
            tailX, tailY = snake.pop()
            graph[tailX][tailY] = 0
    else:
        break

    if turnTime < len(turn) and int(turn[turnTime][0]) == cnt:
        if turn[turnTime][1] == "D":
            head = (head + 1) % 4
        else:
            head = (head + 3) % 4
        turnTime += 1
            
print(cnt)
