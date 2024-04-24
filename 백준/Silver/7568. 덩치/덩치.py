n = int(input())
big = []
score = []
for i in range(n):
    big.append(list(map(int, input().split())))
for i in range(n):
    num = 1
    for w, h in big:
        if big[i][0] < w and big[i][1] < h:
            num +=1        
    score.append(num)
print(*score)