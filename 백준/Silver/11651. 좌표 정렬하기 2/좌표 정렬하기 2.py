num = int(input())
number = [list(map(int, input().split())) for i in range(num)]
number.sort(key = lambda x : (x[1], x[0]))
for i in number:
    print(*i)