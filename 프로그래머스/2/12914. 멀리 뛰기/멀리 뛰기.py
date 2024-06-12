def solution(n):
    answer = [1]*(n+1)
    answer[1] = 2
    
    for i in range(2, n+1):
        answer[i] = (answer[i-1] + answer[i-2]) % 1234567
    
    return answer[-2]