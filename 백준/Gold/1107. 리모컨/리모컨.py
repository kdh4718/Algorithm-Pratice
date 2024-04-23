target = int(input())
answer = abs(100 - target) 
M = int(input())
if M: 
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001): 
    for N in str(num):
        if N in broken: 
            break
    else: 
        answer = min(answer, len(str(num)) + abs(num - target))

print(answer)