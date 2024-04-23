num = int(input())
maxN, count, numL = num, 1, [num]
for i in range(8):
    num = int(input())
    if num > max(numL):
        maxN = num
        count = i+2
    numL.append(num)
print(maxN)
print(count)