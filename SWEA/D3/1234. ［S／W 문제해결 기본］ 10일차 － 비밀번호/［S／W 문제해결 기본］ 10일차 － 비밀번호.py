for test_case in range(1, 11):
    n, number = map(str, input().split())
    numberList = list(number)
    stack = []

    for num in numberList:
        if not stack or stack[-1] != num:
            stack.append(num)
        else:
            stack.pop()

    print(f"#{test_case}", "".join(stack))