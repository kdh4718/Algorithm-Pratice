from itertools import combinations as cb

def solution(orders, course):
    answer = []
    dic = dict()
    result = [[] for _ in range(11)]
    
    for order in orders:
        for n in course:
            for sub in cb(order, n):
                sub = ''.join(sorted(sub))
                
                dic[sub] = dic.get(sub, 0) + 1
    
    for n in course:
        max_count = 2 
        temp = []
        for key, value in dic.items():
            if len(key) == n and value > max_count:
                max_count = value
        
        for key, value in dic.items():
            if len(key) == n and value == max_count:
                temp.append(key)
        
        answer.extend(temp)
            
    return sorted(answer)