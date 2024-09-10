import sys
n = sys.stdin.readline()
a = set(sys.stdin.readline().split())
m = sys.stdin.readline()
b = sys.stdin.readline().split()
for i in b:
    sys.stdout.write('1\n') if i in a else sys.stdout.write('0\n')