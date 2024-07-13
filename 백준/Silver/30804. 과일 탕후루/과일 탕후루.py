n = int(input())
fruits = list(map(int, input().split()))

start = 0
max_length = 0
dic = {}

for end in range(n):
    if fruits[end] in dic:
        dic[fruits[end]] += 1
    else:
        dic[fruits[end]] = 1

    while len(dic) > 2:
        dic[fruits[start]] -= 1
        if dic[fruits[start]] == 0:
            del dic[fruits[start]]
        start += 1

    max_length = max(max_length, end - start + 1)

print(max_length)