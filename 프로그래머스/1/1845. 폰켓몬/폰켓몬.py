def solution(nums):
    answer = 0
    dic = {i: 1 for i in nums}

    return min(len(nums)//2, len(dic))