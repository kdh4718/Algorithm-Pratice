def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.sort()
    score = 0
    for i in range(len(answer)):
        score += answer[i]*(10**i)
    return score