from collections import Counter

def solution(array):
    answer = list(Counter(array).items())
    answer.sort(key = lambda x : x[1])
    
    if len(answer) == 1:
        return answer[0][0]
    
    return answer[-1][0] if answer[-1][1] != answer[-2][1] else -1