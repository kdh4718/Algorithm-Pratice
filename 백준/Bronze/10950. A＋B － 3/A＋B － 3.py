count  = int(input())
numList = []
for i in range(0, count):
    a, b = map(int, input().split())
    numList.append(a+b)
for i in range(0, count):
    print(numList[i])