n = int(input())
room = []
for i in range(n):
    room.append(list(map(int, input().split())))
    
room.sort(key = lambda x: (x[1], x[0]))
count = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        count +=1
        end = room[i][1]
print(count)