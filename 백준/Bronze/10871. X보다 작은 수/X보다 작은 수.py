count, num = map(int, input().split())
numList = []
numList = map(int,input().split())

answerList = []
for i in numList:
    if (i < num): answerList.append(i) 
print(*answerList)