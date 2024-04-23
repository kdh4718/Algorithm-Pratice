n = int(input())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(3):
        l_min = min(rgb[i-1][:j]) if rgb[i-1][:j] else 1e9
        r_min = min(rgb[i-1][j+1:]) if rgb[i-1][j+1:] else 1e9
        rgb[i][j] += min(l_min, r_min)
print(min(rgb[-1]))