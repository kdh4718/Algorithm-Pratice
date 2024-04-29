def hanoi(n, s, e, v):
    if n == 1:
        move.append([s, e])
    else:
        hanoi(n-1, s, v, e)
        move.append([s, e])
        hanoi(n-1, v, e, s)
n = int(input())
move = []
hanoi(n, 1, 3, 2)
print(len(move))
for i in move:
    print(*i)