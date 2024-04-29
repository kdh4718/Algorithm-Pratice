num = int(input())
number = [list(map(int, input().split())) for i in range(num)]
for i in sorted(number):
    print(*i)