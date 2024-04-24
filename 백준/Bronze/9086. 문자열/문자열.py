number = int(input())
fl = []
for i in range(number):
    word = list(input())
    fl.append(word[0]+word[-1])
    
for i in fl:
    print(i)