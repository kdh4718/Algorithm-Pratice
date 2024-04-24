import sys
num = sys.stdin.readline()
number = [int(sys.stdin.readline()) for i in range(int(num))]
for i in sorted(number):
    print(i)