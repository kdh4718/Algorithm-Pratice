def solution(arr1, arr2):
    answer = [[sum(a*b for a, b in zip(row1, col2)) for col2 in zip(*arr2)] for row1 in arr1]
    
    return answer