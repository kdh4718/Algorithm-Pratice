import sys

input = sys.stdin.readline
n, m = map(int, input().split())
book = {}
for i in range(1, n+1):
    write = input().rstrip()
    book[write] = i
    book[i] = write
    
for i in range(m):
    answer = input().rstrip()
    if answer.isdigit():
        print(book[int(answer)])
    else:
        print(book[answer])