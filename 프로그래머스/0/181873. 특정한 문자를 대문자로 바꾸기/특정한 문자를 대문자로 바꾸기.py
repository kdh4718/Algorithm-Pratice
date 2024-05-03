def solution(my_string, alp):
    answer = [i if i not in alp else i.upper() for i in my_string]
    return ''.join(answer)