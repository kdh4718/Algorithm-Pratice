def solution(k, score):
    answer = []
    honor = []
    
    for num in score:
        honor.append(num)
        if len(honor) <= k:
            answer.append(min(honor))
            
        else:
            honor.pop(honor.index(min(honor)))
            answer.append(min(honor))
    
    return answer