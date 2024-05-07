def solution(A,B):
    answer = [a*b for a, b in zip(sorted(A), sorted(B, reverse = True))]

    return sum(answer)