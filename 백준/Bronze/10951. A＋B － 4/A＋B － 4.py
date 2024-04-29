sumList = []
while True:
    try:
        a, b = map(int, input().split())
        sumList.append(a+b)
    except:
        break
        
for i in sumList:
    print(i)