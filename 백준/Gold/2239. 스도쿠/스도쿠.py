graph = [list(map(int, input())) for _ in range(9)]

def check(x, y, num):
    for i in range(9):
        if graph[x][i] == num:
            return False
    for i in range(9):
        if graph[i][y] == num:
            return False
    x = (x // 3) * 3
    y = (y // 3) * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if graph[i][j] == num:
                return False
    return True

def sudoku(x, y):
    if y == 9:
        x += 1
        y = 0
    if x == 9:
        for g in graph:
            print("".join(map(str, g)))
        exit()
    if graph[x][y] != 0:
        sudoku(x, y + 1)
    else:
        for i in range(1, 10):
            if check(x, y, i):
                graph[x][y] = i
                sudoku(x, y + 1)
                graph[x][y] = 0
    return

sudoku(0, 0)
