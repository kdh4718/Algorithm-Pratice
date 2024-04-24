n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def is_white_or_blue(x, y, N):
    global blue, white
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != color:
                is_white_or_blue(x, y, N//2)
                is_white_or_blue(x, y+ N//2, N//2)
                is_white_or_blue(x + N//2, y, N//2)
                is_white_or_blue(x + N//2, y + N//2, N//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
    return
    
is_white_or_blue(0, 0, n)
print(white)
print(blue)