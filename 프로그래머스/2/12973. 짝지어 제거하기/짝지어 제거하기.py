def solution(s):
    answer = []
    
    for i in s:
        if not answer:
            answer.append(i)
            continue
        
        if answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)

    return 0 if answer else 1