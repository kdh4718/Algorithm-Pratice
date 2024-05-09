import itertools

def solution(numbers):
    answer = set([sum(i) for i in itertools.permutations(numbers, 2)])
    
    return sorted(list(answer))