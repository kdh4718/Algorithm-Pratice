nine = [list(map(int, input().split())) for i in range(9)]
maxnum = max(map(max, nine))
maxcol, maxrow = 0, 0
for i in range(9):
    for j in range(9):
        if nine[i][j] == maxnum:
            maxrow = i+1
            maxcol = j+1
        
print(maxnum)
print(maxrow, maxcol)