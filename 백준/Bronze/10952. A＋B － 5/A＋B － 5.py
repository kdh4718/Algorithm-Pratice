sumList = []
while (True):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break;
    else:
        sumList.append(a+b)
for i in sumList:
    print(i)