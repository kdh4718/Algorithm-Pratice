from collections import deque

def ConveyorBelt(n, k, belt):
    answer = 0
    conveyorBelt = deque([False]*n)

    while True:
        answer += 1

        belt.rotate(1)
        conveyorBelt.rotate(1)
        conveyorBelt[n-1] = False
        
        for i in range(n-2, -1, -1):
            if conveyorBelt[i] and not conveyorBelt[i+1] and belt[i+1] > 0:
                conveyorBelt[i], conveyorBelt[i+1] = False, True
                belt[i+1] -= 1
    
        conveyorBelt[n-1] = False
    
        if belt[0] > 0:
            belt[0] -= 1
            conveyorBelt[0] = True
    
        if belt.count(0) >= k:
            return answer
    return answer

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
print(ConveyorBelt(n, k, belt))