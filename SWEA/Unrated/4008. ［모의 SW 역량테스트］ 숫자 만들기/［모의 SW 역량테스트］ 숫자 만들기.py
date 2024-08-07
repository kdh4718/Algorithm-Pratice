import math

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    op = list(map(int, input().split()))
    number = list(map(int, input().split()))
    maxNum, minNum = -float('inf'), float('inf')

    def calculate(i, num, plus, minus, multi, divide):
        global maxNum, minNum
        if i >= len(number):
            if num > maxNum:
                maxNum = num
            if num < minNum:
                minNum = num

            return

        if plus:
            calculate(i+1, num + number[i], plus-1, minus, multi, divide)
        if minus:
            calculate(i+1, num - number[i], plus, minus-1, multi, divide)
        if multi:
            calculate(i+1, num * number[i], plus, minus, multi-1, divide)
        if divide:
            calculate(i+1, math.trunc(num / number[i]), plus, minus, multi, divide-1)

        return

    calculate(1, number[0], op[0], op[1], op[2], op[3])

    print(f"#{test_case}", maxNum - minNum)
