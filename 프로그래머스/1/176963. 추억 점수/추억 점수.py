def solution(name, yearning, photo):
    answer = []
    match = dict()
    
    for n, y in zip(name, yearning):
        match[n] = y
    
    for pho in photo:
        num = 0
        
        for p in pho:
            if p in match:
                num += match[p]
            
        answer.append(num)
    
    return answer