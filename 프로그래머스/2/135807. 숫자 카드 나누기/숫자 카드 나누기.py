from math import gcd
from functools import reduce

def findGcd(array):
    return reduce(gcd, array)

def check(div, array):
    for num in array:
        if num % div == 0:
            return False
    
    return True

def solution(arrayA, arrayB):
    answer = 0
    
    gcdA = findGcd(arrayA)
    gcdB = findGcd(arrayB)
    
    if check(gcdA, arrayB):
        answer = max(answer, gcdA)
    if check(gcdB, arrayA):
        answer = max(answer, gcdB)
    
    return answer