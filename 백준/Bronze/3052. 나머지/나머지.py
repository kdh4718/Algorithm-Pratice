number = []
for i in range(10):
    num = int(input())
    number.append(num%42)
number = list(set(number))
print(len(number))