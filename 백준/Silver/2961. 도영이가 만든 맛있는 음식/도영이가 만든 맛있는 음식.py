n = int(input())
food = [list(map(int, input().split())) for _ in range(n)]
minimum = float('inf')

def mixingFood(index, sour, bitter):
    global minimum
    if index >= n:
        return
    minimum = min(minimum, abs(sour - bitter))
    mixingFood(index+1, sour, bitter)

    sour *= food[index][0]
    bitter += food[index][1]
    minimum = min(minimum, abs(sour - bitter))
    mixingFood(index + 1, sour, bitter)

for i in range(n):
    sour, bitter = food[i][0], food[i][1]
    minimum = min(minimum, abs(sour - bitter))
    mixingFood(i+1, sour, bitter)

print(minimum)