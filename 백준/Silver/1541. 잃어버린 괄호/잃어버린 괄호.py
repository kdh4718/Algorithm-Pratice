import re
line = re.split('([+-])', input())
num = 0
number = []

for i in range(2, len(line), 2):
    if line[i-1] == "+":
        line[i] = str(int(line[i]) + int(line[i-2]))
        line[i-2] = "0"
        
for i in line:
    if i.isdigit() and i != "0":
        number.append(i)
        
num = int(number[0])
for i in range(1, len(number)):
    num -= int(number[i])
    
print(num)