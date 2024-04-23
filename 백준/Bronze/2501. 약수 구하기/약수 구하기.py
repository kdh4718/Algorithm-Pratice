a, b = map(int, input().split())
div = []

for i in range(1, a+1):
    if a % i == 0:
        div.append(i)
        
if len(div) > b-1:
    print(div[b-1])
else:
    print(0)