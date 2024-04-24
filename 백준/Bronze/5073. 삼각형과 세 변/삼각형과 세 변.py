while True:
    a, b, c = map(int, input().split())
    tri = [a, b, c]
    tri.sort()
    if sum(tri) == 0:
        break
    elif tri[0] + tri[1] <= tri[2]:
        print("Invalid")
    elif tri[0] == tri[2]:
        print("Equilateral")
    elif tri[0] == tri[1] or tri[1] == tri[2]:
        print("Isosceles")
    else:
        print("Scalene")