def solution(s):
    answer = []
    dic = dict()
    
    for i, j in enumerate(s):
        if j not in dic:
            answer.append(-1)
            dic[j] = i
        else:
            answer.append(i - dic[j])
            dic[j] = i
    
    return answer