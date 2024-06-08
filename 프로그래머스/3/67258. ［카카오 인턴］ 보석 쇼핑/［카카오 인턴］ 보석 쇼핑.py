def solution(gems):
    size = len(set(gems))
    gem_dict = {gems[0]: 1}
    temp = [0, len(gems) - 1]  # 초기 범위
    start, end = 0, 0

    while end < len(gems) and start < len(gems):
        if len(gem_dict) == size:  # 모든 종류의 보석을 찾았다면
            if end - start < temp[1] - temp[0]:  # 기존의 범위보다 짧으면 갱신
                temp = [start, end]
            if gem_dict[gems[start]] == 1:  # start 위치의 보석이 1개라면 dict에서 제거
                del gem_dict[gems[start]]
            else:
                gem_dict[gems[start]] -= 1
            start += 1  # start를 오른쪽으로 이동
        else:
            end += 1  # end를 오른쪽으로 이동
            if end == len(gems):  # 범위를 벗어나면 종료
                break
            if gems[end] in gem_dict.keys():  # 보석이 이미 dict에 있다면 개수 증가
                gem_dict[gems[end]] += 1
            else:  # 새로운 보석이라면 dict에 추가
                gem_dict[gems[end]] = 1

    return [temp[0]+1, temp[1]+1]
