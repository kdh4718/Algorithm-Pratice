def solution(arr1, arr2):
    answer = [[sum(a*b for a, b in zip(row1, col1)) for col1 in zip(*arr2)] 
             for row1 in arr1]
    
    return answer