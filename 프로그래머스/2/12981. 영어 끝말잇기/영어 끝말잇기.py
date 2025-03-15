def solution(n, words):
    wordList = dict()
    
    for i in range(len(words)):
        if not wordList:
            wordList[words[i]] = i
            continue
        
        if words[i] in wordList or words[i-1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]
        
        wordList[words[i]] = i
    
    return [0, 0]
