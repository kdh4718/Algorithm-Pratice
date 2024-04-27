num = int(input())
person = [list(map(str, input().split())) for i in range(num)]
person.sort(key = lambda x : int(x[0]))
for i in person:
    print(*i)