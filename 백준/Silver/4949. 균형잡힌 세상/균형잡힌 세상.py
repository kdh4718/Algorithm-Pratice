while True:
    a = input()
    if a == '.':
        break
    stack = []
    is_balance = True  

    for i in a:
        if i in '([':
            stack.append(i)
        elif i in ')]':
            if not stack:
                is_balance = False
                break
            top = stack.pop()
            if (i == ')' and top != '(') or (i == ']' and top != '['):
                is_balance = False
                break

    if not stack and is_balance:
        print('yes')
    else:
        print('no')