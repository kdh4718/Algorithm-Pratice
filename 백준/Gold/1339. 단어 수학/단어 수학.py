n = int(input())
words = [list(input()) for _ in range(n)]
dic = dict()
answer = 0
num = 9

for word in words:
    x = len(word) - 1
    for i in word:
        if i in dic:
            dic[i] += 10 ** x
        else:
            dic[i] = 10 ** x

        x -= 1

words = sorted(dic.values(), reverse=True)

for word in words:
    answer += word * num
    num -= 1

print(answer)
