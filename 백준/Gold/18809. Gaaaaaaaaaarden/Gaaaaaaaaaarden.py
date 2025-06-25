from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

def bfs(green, red):
    q = deque()
    state = [[(-1, 0)] * m for _ in range(n)]
    for gx, gy in green:
        q.append((gx, gy, 0, 1))
        state[gx][gy] = (0, 1)
    for rx, ry in red:
        q.append((rx, ry, 0, 2))
        state[rx][ry] = (0, 2)

    flower = 0
    while q:
        x, y, t, color = q.popleft()
        if state[x][y][1] == 3:
            continue
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and garden[nx][ny] != 0:
                nt, nc = state[nx][ny]
                if nc == 0:
                    state[nx][ny] = (t + 1, color)
                    q.append((nx, ny, t + 1, color))
                elif nc != color and nt == t + 1 and nc != 3:
                    state[nx][ny] = (t + 1, 3)
                    flower += 1
    return flower

n, m, g, r = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(n)]
seed_spots = [(i, j) for i in range(n) for j in range(m) if garden[i][j] == 2]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0
for positions in combinations(seed_spots, g + r):
    for greens in combinations(positions, g):
        reds = [pos for pos in positions if pos not in greens]
        answer = max(answer, bfs(greens, reds))

print(answer)
