import math

twoFour = [2, 4]
n = int(input())

for _ in range(n):
    square = [list(map(int, input().split())) for _ in range(4)]
    dic = dict()

    def checkSquare():
        for i in range(4):
            for j in range(i+1, 4):
                distance = math.sqrt(math.pow(square[i][0] - square[j][0], 2) + math.pow(square[i][1] - square[j][1], 2))
                if distance not in dic:
                    dic[distance] = 1
                else:
                    dic[distance] += 1

        if len(dic) != 2:
            return 0

        listD = list(dic.items())
        if listD[0][1] not in twoFour:
            return 0

        return 1

    print(checkSquare())