n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
dice = [0]*6
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def turn(dir):
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif dir == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

for order in orders:
    nx = x + dx[order]
    ny = y + dy[order]

    if 0 <= nx < n and 0<= ny < m:
        x, y = nx, ny
        turn(order)
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[0])
        
    else:
        continue