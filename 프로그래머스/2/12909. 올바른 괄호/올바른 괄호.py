def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == ')':
            if not stack:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        else:
            stack.append(i)

    if stack:
        return False
    return True