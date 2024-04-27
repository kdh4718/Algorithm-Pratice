numn, numm = map(int, input().split())
number = []
for i in range(numn):
    number.append(i+1)

for i in range(numm):
    revs, reve = map(int, input().split())
    number[revs-1:reve] = list(reversed(number[revs-1:reve]))
    
print(*number)