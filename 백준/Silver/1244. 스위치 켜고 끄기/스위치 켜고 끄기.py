n = int(input())
onOff = list(map(int, input().split()))
student = int(input())
dic = {0: 1, 1: 0}

for _ in range(student):
    male, num = map(int, input().split())

    if male == 1:
        for i in range(num-1, len(onOff), num):
            onOff[i] = dic[onOff[i]]
    else:
        onOff[num-1] = dic[onOff[num-1]]
        left, right = num-2, num

        while 0 <= left and right < len(onOff) and onOff[left] == onOff[right]:
            onOff[left] = dic[onOff[left]]
            onOff[right] = dic[onOff[right]]

            left -= 1
            right += 1

for i in range(len(onOff)):
    print(onOff[i], end = " ")
    if (i+1) % 20 == 0:
        print()