def solution(clothes):
    answer = 1
    dic = dict()
    
    for clo, typ in clothes:
        if typ not in dic:
            dic[typ] = 2
        else:
            dic[typ] += 1
    
    for i in dic.values():
        answer *= i
    
    return answer - 1