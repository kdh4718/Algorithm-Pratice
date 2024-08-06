from itertools import combinations as cb

while True:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break

    lotto = lotto[1:]
    numberList = cb(lotto, 6)
    
    for num in numberList:
        print(*sorted(num))
    print()
