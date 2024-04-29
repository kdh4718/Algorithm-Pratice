n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

fuel = city[0]
cost = 0
loc = 0
leng = road[0]

for i in range(1, n-1):
    if city[i] < fuel:
        cost += city[loc]*leng
        loc = i
        fuel = city[i]
        leng = road[i]
    else:
        leng += road[i]
    
    if i == n-2:
        cost += city[loc]*leng

print(cost)