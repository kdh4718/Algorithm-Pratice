def solution(storey):
    answer = 0
    
    while storey != 0:
        num = storey % 10
        
        if num > 5 or (num == 5 and storey % 100 >= 50): 
            answer += 10 - num
            storey += 10
        else: 
            answer += num
            
        storey //= 10
    
    return answer