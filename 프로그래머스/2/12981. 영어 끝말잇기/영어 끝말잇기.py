def solution(n, words):
    answer = [2, 1]
    wordList = []
    
    for i in range(len(words)):
        if not wordList: 
            wordList.append(words[i])
            continue
        
        if words[i] in wordList or wordList[-1][-1] != words[i][0]:
            return answer
        
        if answer[0] == n:
            answer[0] = 1
            answer[1] += 1
        else:
            answer[0] += 1
        wordList.append(words[i])

    return [0, 0]