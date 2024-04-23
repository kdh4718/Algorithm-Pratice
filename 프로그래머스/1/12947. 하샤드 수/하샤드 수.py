def solution(x):
    answer = True
    divide = 0
    for i in str(x):
        divide += int(i)
    if x % divide == 0:
        answer = True
    else:
        answer = False
    return answer