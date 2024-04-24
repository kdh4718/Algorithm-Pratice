count = int(input())
coin = [[0 for i in range(4)] for i in range(count)]
for i in range(count):
    cost = int(input())
    coin[i][0] = cost//25
    cost %= 25
    coin[i][1] = cost//10
    cost %= 10
    coin[i][2] = cost//5
    cost %= 5
    coin[i][3] = cost

for i in range(count):
    print(*coin[i])