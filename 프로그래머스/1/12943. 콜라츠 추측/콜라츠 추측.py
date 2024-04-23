def solution(num):
    answer = 0
    while answer < 500:
        if num == 1:
            break
        if num % 2 == 0:
            num /= 2
            answer += 1
            continue
        else:
            num *= 3
            num += 1
            answer += 1
    if answer == 500:
        return -1
    return answer