number = int(input())
for i in range(number):
    num, word = map(str, input().split())
    for i in word:
        print(i*int(num), end = '')
    print()