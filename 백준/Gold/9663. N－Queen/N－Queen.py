def collect(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x]-board[i]) == x-i:
            return False
    return True
def queen(x):
    global count
    if x == n:
        count += 1
        return
    else:
        for i in range(n):
            board[x] = i
            if collect(x):
                queen(x+1)
n = int(input())
board = [0]*n
count = 0
queen(0)
print(count)