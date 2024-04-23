num = int(input())
word = [input() for i in range(num)]
word = list(set(word))
word.sort(key = lambda x: (len(x), x))
for i in word:
    print(i)