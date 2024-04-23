def solution(n, works):
    if len(works) == 1:
        return (works[0]-n)**2
    len_works = len(works)
    answer = sum(works)-n
    if answer < 1:
        return 0
    works.sort(reverse = True)
    loc = 1
    while n>0:
        if works[0] > works[loc]:
            for i in range(loc):
                works[i] -= 1
                n -= 1
                if n == 0: 
                    break
        else:
            if loc == len_works-1:
                works[loc] -= 1
                n -= 1
            else:
                loc += 1               
        
    return sum(i*i for i in works)