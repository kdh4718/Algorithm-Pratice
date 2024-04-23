count = [0]*10
a = int(input())
b = int(input())
c = int(input())
d = a*b*c
for i in str(d):
    count[int(i)] += 1
for i in count:
    print(i)