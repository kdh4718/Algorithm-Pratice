n, s = map(int, input().split())
number = list(map(int, input().split()))
minimum = 1e9
start = 0
sumNum = 0

for end in range(len(number)):
    sumNum += number[end]

    while sumNum >= s:
        minimum = min(minimum, end - start + 1)
        sumNum -= number[start]
        start += 1

print(minimum if minimum != 1e9 else 0)