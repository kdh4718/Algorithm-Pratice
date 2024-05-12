def solution(k, score):
    answer = []
    honor = []
    
    for num in score:
        honor.append(num)
        if len(honor) > k:
            honor.remove(min(honor))

        answer.append(min(honor))
    
    return answer