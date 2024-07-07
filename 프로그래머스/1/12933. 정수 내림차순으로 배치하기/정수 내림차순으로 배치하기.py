def solution(n):
    return int(''.join(sorted(list(i for i in str(n)), reverse = True)))