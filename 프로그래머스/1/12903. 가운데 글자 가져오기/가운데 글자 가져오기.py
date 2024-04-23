def solution(s):
    answer = list(s)
    while len(answer) > 2:
        answer.pop(0)
        answer.pop()
    answer = "".join(answer)
    return answer