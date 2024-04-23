y, x = map(int, input().split())
board = []

for i in range(y):
    board.append(input())
mincount = []
for i in range(y-7):
    for j in range(x-7):
        white_count = 0
        black_count = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l)%2 == 0:
                    if board[k][l] == 'B':
                        white_count += 1
                    else:
                        black_count += 1
                else:
                    if board[k][l] == 'B':
                        black_count += 1
                    else:
                        white_count += 1
        mincount.append(white_count)
        mincount.append(black_count)
                    
print(min(mincount))                  