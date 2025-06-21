def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    
    for i in reserve[:]:
        if i in lost:
            answer += 1
            lost.remove(i)
            reserve.remove(i)
            
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
            answer += 1
            
        elif i+1 in lost:
            lost.remove(i+1)
            answer += 1
        
    return answer