num = int(input())
minx, miny = [], []
for i in range(num):
    x, y = map(int, input().split())
    minx.append(x)
    miny.append(y)
print((max(minx)-min(minx))*(max(miny)-min(miny)))