from itertools import combinations

def solution(number):
    answer = 0
    three_number = combinations(number, 3)
    
    for num in three_number:
        if sum(num) == 0:
            answer += 1
    
    return answer