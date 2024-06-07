def solution(book_time):
    answer = []
    book_time.sort(key = lambda x: x[0])
    
    def time(t):
        t = list(t.split(":"))
        t = list(int(i) for i in t)
        if t[1] >= 50:
            t[0] += 1
            t[1] -= 50
        else:
            t[1] += 10
        
        return t
    
    for start, end in book_time:
        start_time = list(start.split(":"))
        start_time = list(int(i) for i in start_time)
        end_time = time(end)
        flag = False
        
        if not answer:  
            answer.append(end_time)
            continue
            
        for i in range(len(answer)):
            hour = (start_time[0] - answer[i][0])*60
            minute = (start_time[1] - answer[i][1])

            if (hour + minute) >= 0:
                answer[i] = end_time
                flag = True
                break
        
        if not flag:
            answer.append(end_time)
    
    return len(answer)