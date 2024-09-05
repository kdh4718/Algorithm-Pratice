test_case = int(input())

def charge(ay, ax, by, bx):
    charge_a_list = []
    charge_b_list = []
    for y, x, c, p, n in charge_info:
        if abs(ay - y) + abs(ax - x) <= c:
            charge_a_list.append([p, n])
        if abs(by - y) + abs(bx - x) <= c:
            charge_b_list.append([p, n])

    charge_a_list.sort(key=lambda x: -x[0])
    charge_b_list.sort(key=lambda x: -x[0])

    temp_a = 0
    flag = 0
    for p, n in charge_a_list:
        temp_a += p
        flag = n
        break

    for p, n in charge_b_list:
        if n != flag:
            temp_a += p
            break

    temp_b = 0
    flag = 0
    for p, n in charge_b_list:
        temp_b += p
        flag = n
        break

    for p, n in charge_a_list:
        if n != flag:
            temp_b += p
            break

    return max(temp_a, temp_b)

for tc in range(test_case):
    N = 10
    M, A = map(int, input().split())
    move_info = [list(map(int, input().split())) for _ in range(2)]
    charge_info = []
    for a in range(A):
        x, y, c, p = map(int, input().split())
        charge_info.append([y, x, c, p, a+1])

    dy = [0, -1, 0, 1, 0]
    dx = [0, 0, 1, 0, -1]
    answer = charge(1, 1, N, N)
    ay, ax, by, bx = 1, 1, N, N
    for d in range(M):
        ay += dy[move_info[0][d]]
        ax += dx[move_info[0][d]]
        by += dy[move_info[1][d]]
        bx += dx[move_info[1][d]]
        answer += charge(ay, ax, by, bx)

    print("#{} {}".format(tc+1, answer))