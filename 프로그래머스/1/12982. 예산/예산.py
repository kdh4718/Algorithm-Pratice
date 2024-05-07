def solution(d, budget):
    answer = 0
    
    for i in sorted(d):
        if i > budget:
            break
        else:
            budget -= i
            answer += 1
    
    return answer