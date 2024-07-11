from collections import deque

# 4개의 톱니바퀴를 입력 받음
gear = [deque(map(int, input().strip())) for _ in range(4)]
k = int(input())

def determine_turn_directions(n, d, directions):
    directions[n] = d
    left_turn(n, d, directions)
    right_turn(n, d, directions)

def left_turn(n, d, directions):
    if n > 0 and directions[n-1] == 0 and gear[n][6] != gear[n-1][2]:
        directions[n-1] = -d
        left_turn(n-1, -d, directions)

def right_turn(n, d, directions):
    if n < 3 and directions[n+1] == 0 and gear[n][2] != gear[n+1][6]:
        directions[n+1] = -d
        right_turn(n+1, -d, directions)

# K번 회전 명령을 입력 받음
for _ in range(k):
    n, d = map(int, input().split())
    n -= 1  # 톱니바퀴 번호는 1부터 시작하므로 0부터 시작하도록 조정

    # 톱니바퀴 회전 방향 초기화
    directions = [0] * 4
    determine_turn_directions(n, d, directions)
    
    # 톱니바퀴 회전 적용
    for i in range(4):
        if directions[i] != 0:
            gear[i].rotate(directions[i])

# 결과 계산
result = 0
result += 1 if gear[0][0] == 1 else 0
result += 2 if gear[1][0] == 1 else 0
result += 4 if gear[2][0] == 1 else 0
result += 8 if gear[3][0] == 1 else 0

print(result)
