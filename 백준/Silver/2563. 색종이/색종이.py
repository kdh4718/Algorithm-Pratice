num = int(input())
sumnum = 0
white_paper = [[0 for j in range(100)] for i in range(100)]

for i in range(num):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            white_paper[i][j] = 1
for i in range(100):
    sumnum += white_paper[i].count(1)
print(sumnum)