num = int(input())
minnum = 0
for i in range(1, num+1):
    div = sum(map(int, str(i)))
    if div + i == num:
        minnum = i
        break

print(minnum)