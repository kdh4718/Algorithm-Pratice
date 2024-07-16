n = int(input())
bestFriend = [list(map(int, input().split())) for _ in range(n*n)]
shark = [[0]*n for _ in range(n)]
happy = 0
happyScore = [0, 1, 10, 100, 1000]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def checkFriends(x, y, num):
    myFriend = []
    cnt = 0
    
    for friend in bestFriend:
        if friend[0] == num:
            myFriend = friend[1:]
            break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if shark[nx][ny] in myFriend:
                cnt += 1
    
    return cnt

for friend in bestFriend:
    num, *friends = friend
    best_positions = []
    max_friends = -1
    
    for i in range(n):
        for j in range(n):
            if shark[i][j] == 0:
                count = checkFriends(i, j, num)
                if count > max_friends:
                    max_friends = count
                    best_positions = [(i, j)]
                elif count == max_friends:
                    best_positions.append((i, j))
    
    if len(best_positions) == 1:
        x, y = best_positions[0]
    else:
        max_empty = -1
        best_final_positions = []
        for x, y in best_positions:
            empty_count = sum(
                1 for d in range(4)
                if 0 <= x + dx[d] < n and 0 <= y + dy[d] < n and shark[x + dx[d]][y + dy[d]] == 0
            )
            if empty_count > max_empty:
                max_empty = empty_count
                best_final_positions = [(x, y)]
            elif empty_count == max_empty:
                best_final_positions.append((x, y))
        
        x, y = min(best_final_positions)
    
    shark[x][y] = num

for i in range(n):
    for j in range(n):
        happy += happyScore[checkFriends(i, j, shark[i][j])]

print(happy)