def solution(s):
    answer = [int(i) for i in s.split()]
    return str(min(answer)) + " " + str(max(answer))