stu, good = [], []
for i in range(1, 31):
    stu.append(i)
for i in range(28):
    a = int(input())
    good.append(a)
stu = [x for x in stu if x not in good]
for i in stu:
    print(i)