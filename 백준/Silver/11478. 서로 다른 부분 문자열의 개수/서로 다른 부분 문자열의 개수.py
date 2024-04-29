word = input()
answer = {}
for i in range(len(word)+1):
    for j in range(i):
        answer[word[j:i]] = 1
print(len(answer.keys()))