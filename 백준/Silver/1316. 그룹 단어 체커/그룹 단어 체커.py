num = int(input())
count = 0
for i in range(num):
    word = list(input())
    while len(word) > 1:
        tar = word[0]
        word.pop(0)
        if tar in word and word[0] != tar:
            count -= 1
            break
        else:
            continue
    count +=1
print(count)