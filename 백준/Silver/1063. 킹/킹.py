dic = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0], 'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}
king, stone, t = map(str, input().split(" "))
moves = [input() for _ in range(int(t))]
kx, ky = 9 - abs(int(king[1])), abs(ord(king[0]) - 65 + 1)
sx, sy = 9 - abs(int(stone[1])), abs(ord(stone[0]) - 65 + 1)

for move in moves:
    nkx = kx + dic[move][0]
    nky = ky + dic[move][1]

    if not (0 < nkx <= 8 and 0 < nky <= 8): continue
    if nkx == sx and nky == sy:
        nsx = sx + dic[move][0]
        nsy = sy + dic[move][1]

        if not (0 < nsx <= 8 and 0 < nsy <= 8): continue

        kx, ky = nkx, nky
        sx, sy = nsx, nsy
    else:
        kx, ky = nkx, nky

print(''.join([str(chr(ky + 65 - 1)), str(9 - kx)]))
print(''.join([str(chr(sy + 65 - 1)), str(9 - sx)]))
