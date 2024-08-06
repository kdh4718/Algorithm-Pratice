for test_case in range(1, 11):
    n = int(input())
    calculate = list(input())
    stack = []
    operator = []
    rpn = []
    result = 0
    prior = {"*": 2, "+": 1, "(": 0}

    for cal in calculate:
        if cal.isdigit():
            rpn.append(cal)
        elif cal == "(":
            operator.append(cal)
        elif cal == ")":
            while operator[-1] != "(":
                rpn.append(operator.pop())
            operator.pop()
        else:
            while operator and prior[cal] <= prior[operator[-1]]:
                rpn.append(operator.pop())
            operator.append(cal)

    while operator:
        rpn.append(operator.pop())

    for r in rpn:
        if r.isdigit():
            stack.append(r)
        else:
            if r == "*":
                num = int(stack.pop()) * int(stack.pop())
                stack.append(num)
            else:
                num = int(stack.pop()) + int(stack.pop())
                stack.append(num)

    print(f"#{test_case}", stack[0])