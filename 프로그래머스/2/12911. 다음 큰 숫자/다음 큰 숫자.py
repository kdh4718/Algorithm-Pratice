def solution(n):
    cnt = bin(n).count('1')
    num = n+1
    
    while True:
        num_cnt = bin(num).count('1')
        if cnt == num_cnt:
            break
        
        num += 1
    
    return num