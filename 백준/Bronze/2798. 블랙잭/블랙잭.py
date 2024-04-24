count, black = map(int, input().split())
card = list(map(int, input().split()))
number = 0
for i in range(len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            newplus = card[i] + card[j] + card[k]
            if newplus <= black and newplus > number:
                number = newplus
                
print(number)