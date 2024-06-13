from collections import deque
def solution(s):
    result = 0
    s = list(s)
    for j in range(len(s)):
        s.append(s.pop(0))
        answer = []
        for i in s:
            if answer and i == ")" and answer[-1] == "(":
                answer.pop()
            elif answer and i == "]" and answer[-1] == "[":
                answer.pop()
            elif answer and i == "}" and answer[-1] == "{":
                answer.pop()
            else:
                answer.append(i)
        if len(answer) == 0:
            result += 1
    return result