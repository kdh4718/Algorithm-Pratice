def solution(k, tangerine):
    answer = 0
    dic = dict()
    
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    dic = sorted(dic.values(), reverse = True)
    
    for i in dic:
        if k <= 0:
            break
            
        k -= i
        answer += 1
    
    return answer