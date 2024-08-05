for test_case in range(1, 11):
    num = int(input())
    brackets = list(input())
    stack = []
    openBracket = ["(", "{", "[", "<"]
    closeBracket = [")", "}", "]", ">"]
    valid = True  

    for bracket in brackets:
        if bracket in openBracket:
            stack.append(bracket)
        elif bracket in closeBracket:
            if not stack or stack[-1] != openBracket[closeBracket.index(bracket)]:
                valid = False
                break
            stack.pop()

    if stack:
        valid = False

    print(f"#{test_case}", 1 if valid else 0)
