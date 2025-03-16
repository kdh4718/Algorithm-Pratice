from collections import Counter

def solution(nums):
    answer = Counter(nums)
    
    return min(len(answer), len(nums)//2)