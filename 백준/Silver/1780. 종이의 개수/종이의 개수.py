n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
minus = 0
zero = 0
plus = 0

def piece(x, y, N):
    global minus, zero, plus
    point = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != point:
                piece(x, y, N//3)
                piece(x + N//3, y, N//3)
                piece(x, y + N//3, N//3)
                piece(x + N//3, y + N//3, N//3)
                piece(x + (N*2)//3, y, N//3)
                piece(x + (N*2)//3, y + N//3, N//3)
                piece(x, y + (N*2)//3, N//3)
                piece(x + N//3, y + (N*2)//3, N//3)
                piece(x + (N*2)//3, y + (N*2)//3, N//3)
                return
    if point == -1:
        minus += 1
    elif point == 0:
        zero += 1
    else:
        plus += 1

piece(0, 0, n)
print(minus)
print(zero)
print(plus)