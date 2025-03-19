def solution(genres, plays):
    answer = []
    sum_geners = {i:[] for i in set(genres)}
    sum_plays = {i:0 for i in set(genres)}
    
    for gen, ply, i in zip(genres, plays, range(len(plays))):
        sum_geners[gen].append([ply , i])
        sum_plays[gen] += ply
        
    for i, j in sorted(sum_plays.items(), key=lambda x:x[1], reverse=True):
        for k, l in sorted(sum_geners[i], key=lambda x:x[0], reverse=True)[:2]:
            answer.append(l)
    
    return answer