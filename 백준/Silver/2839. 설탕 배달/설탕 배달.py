num = int(input())
count = 0
weight = []
while True: 
    if num == sum(weight) or num < sum(weight):
        break
    else:
        weight.append(5)
        count += 1
while True:
    if num == sum(weight):
        break
    
    if weight.count(5) == 0 and num < sum(weight):
        break
    elif num < sum(weight):
        weight.pop(0)
        count -= 1
        continue
    elif num > sum(weight):
        weight.append(3)
        count +=1
        continue
if num == sum(weight):
    print(count)
else:
    print(-1)