count  = int(input())
numList = []
number = []
for i in range(0, count):
    number.append([])
    a, b = map(int, input().split())
    numList.append(a+b)
    number[i].append(a)
    number[i].append(b)
for i in range(0, count):
    print(f"Case #{i+1}: {number[i][0]} + {number[i][1]} = {numList[i]}")