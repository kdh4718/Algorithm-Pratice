def row(a, n): # 가로
    for i in range(9):
        if n == sudoku[a][i]: 
            return False
    return True

def column(a, n): # 세로
    for i in range(9):
        if n == sudoku[i][a]: 
            return False
    return True

def square(y, x, n): # 3x3 칸
    for i in range(3):
        for j in range(3):
            if n == sudoku[y//3 * 3 + i][x//3 * 3 + j]: 
                return False
    return True

def find(n):
    if n == len(blank): # 빈 공간 만큼 사용했으면
        for i in sudoku: 
            print(*i) 
        exit() 

    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        if column(x,i) and row(y,i) and square(y, x, i):
            sudoku[y][x] = i
            find(n+1)
            sudoku[y][x] = 0

import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])
find(0)