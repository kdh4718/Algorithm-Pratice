def solution(sequence, k):
    answer = [0, len(sequence)]
    start, end = 0, 0
    num = sequence[0]
    
    while start < len(sequence):
        if num < k:
            end += 1
            if end == len(sequence):
                break
            num += sequence[end]
            
        else:
            if num == k and end-start < answer[1]-answer[0]:
                answer = [start, end]
            
            num -= sequence[start]
            start += 1
    
    return answer