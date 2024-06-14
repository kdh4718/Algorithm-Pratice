def solution(nums):
    answer = 0
    dic = {i: 1 for i in nums}
            
    if len(nums)//2 >= len(dic):
        return len(dic)
    else:
        return len(nums)//2
    
    return answer