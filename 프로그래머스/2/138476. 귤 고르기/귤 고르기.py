def solution(k, tangerine):
    answer = 0
    dic = dict()
    
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    
    for t, num in dic:
        if k <= 0:
            break
        
        k -= num
        answer += 1
    
    return answer