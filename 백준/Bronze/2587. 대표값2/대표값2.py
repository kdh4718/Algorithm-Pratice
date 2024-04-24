number = [int(input()) for i in range(5)]
number.sort()
print(int(sum(number)/len(number)))
print(number[2])