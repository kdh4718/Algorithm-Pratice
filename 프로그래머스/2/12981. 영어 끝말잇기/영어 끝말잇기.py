def solution(n, words):
    wordList = []
    
    for i in range(len(words)):
        if not wordList: 
            wordList.append(words[i])
            continue
        
        if words[i] in wordList or wordList[-1][-1] != words[i][0]:
            return [(i%n)+1, (i//n)+1]

        wordList.append(words[i])

    return [0, 0]