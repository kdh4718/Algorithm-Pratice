count = int(input())
numList = []
numList = map(int,input().split())
num = int(input())
count = 0
for i in numList:
    if i == num:
        count += 1
        
print(count)