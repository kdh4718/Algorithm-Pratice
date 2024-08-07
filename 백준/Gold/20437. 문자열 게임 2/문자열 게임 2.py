from collections import defaultdict

t = int(input())

for _ in range(t):
    word = list(input())
    k = int(input())
    lenWord = len(word)
    minNum, maxNum = float('inf'), -1

    pos = defaultdict(list)
    for i in range(lenWord):
        pos[word[i]].append(i)

    for key in pos:
        if len(pos[key]) >= k:
            for i in range(len(pos[key]) - k + 1):
                current_length = pos[key][i + k - 1] - pos[key][i] + 1
                if current_length < minNum:
                    minNum = current_length
                if current_length > maxNum:
                    maxNum = current_length


    if minNum == float('inf') or maxNum == -1:
        print(-1)
    else:
        print(minNum, maxNum)