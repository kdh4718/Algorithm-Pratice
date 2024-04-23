n, c = map(int, input().split())
house = []

for i in range(n):
    house.append(int(input()))
house.sort()  

start = 1
end = house[-1] - house[0]
result = 0

while start <= end:
    mid = (start + end)//2
    
    loc = house[0]
    count = 1
    
    for i in range(1, len(house)):
        if house[i] >= loc + mid:
            count += 1
            loc = house[i]
            
    if count >= c:
        start = mid + 1
        result = mid
    else:    
        end = mid - 1
        
print(result)